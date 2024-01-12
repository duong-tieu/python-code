from math import sin, cos, pi, log
from tkinter import *
import random

CANVAS_WIGTH = 640
CANVAS_HEIGHT = 480
CANVAS_CENTER_X = CANVAS_WIGTH / 2
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
IMAGE_ENLARGE = 11
HEART_COLOR = "#00FF00"
# Text_color = "#FFFF00"

def heart_funtion(t, shrink_ratio: float, CANVAS_CENTER_X, CANVAS_CENTER_Y):
    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
    x *= shrink_ratio
    y *= shrink_ratio

    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y

    return int(x), int(y)


def scatter_inside(x, y, beta=0.15):
    radio_x = -beta * log(random.random())
    radio_y = -beta * log(random.random())

    dx = radio_x * (x - CANVAS_CENTER_X)
    dy = radio_y * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy


def shrink(x, y, ratio):
    force = -1 // (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.6)
    dx = ratio * force * (x - CANVAS_CENTER_X)
    dy = ratio * force * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy


def curve(p):
    return 2 * (2 * sin(4 * p)) / (2 * pi)


class Heart:
    def __init__(self, generate_frame=20):
        self._points = set()
        self._edge_diffusion_points = set()
        self._center_diffusion_points = set()
        self.all_points = {}
        self.build(2000)

        self.random_halo = 1000

        self.generate_frame = generate_frame
        for frame in range(generate_frame):
            self.calc(frame)

    def build(self, number):
        for _ in range(number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_funtion(t, shrink_ratio=IMAGE_ENLARGE, CANVAS_CENTER_X=CANVAS_CENTER_X,
                                 CANVAS_CENTER_Y=CANVAS_CENTER_Y)
            self._points.add((x, y))

        for _x, _y in list(self._points):
            for _ in range(3):
                x, y = scatter_inside(_x, _y, 0.05)
                self._edge_diffusion_points.add((x, y))

    def render(self,render_canvas,render_frame):  # type: ignore
        for x, y , size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x +size,y + size, width= 0, fill = HEART_COLOR)

        center_x = CANVAS_WIGTH / 2
        center_y = CANVAS_HEIGHT / 2           
        render_canvas.create_text(center_x, center_y, text="I love you", fill="white", font=("Helvetica", 12))           

        point_list = list(self._points)
        for _ in range(4000):
            x, y = random.choice(point_list)
            x, y = scatter_inside(x, y, 0.17)
            self._center_diffusion_points.add((x, y))
    
    @staticmethod
    def calc_position(x, y, ratio):
        force = 1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.520)

        dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)

        return x - dx, y - dy

    def calc(self, generate_frame):
        ratio = 10 * curve(generate_frame / 10 * pi)
        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))

        all_points = []

        heart_halo_point = set()
        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_funtion(t, shrink_ratio=11.6, CANVAS_CENTER_X=CANVAS_CENTER_X,
                                 CANVAS_CENTER_Y=CANVAS_CENTER_Y)
            x, y = shrink(x, y, halo_radius)
            if (x, y) not in heart_halo_point:
                heart_halo_point.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_points.append((x, y, size))

        for x, y in self._points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 3)
            all_points.append((x, y, size))

        for x, y in self._edge_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        for x, y in self._center_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        self.all_points[generate_frame] = all_points

    def render(self, render_canvas, render_frame):
        for x, y, size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)


def draw(main: Tk, render_canvas: Canvas, render_heart: Heart, render_frame=0):
    render_canvas.delete("all")
    render_heart.render(render_canvas, render_frame)
    main.after(160, draw, main, render_canvas, render_heart, render_frame + 1)

if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIGTH)
    canvas.pack()
    heart = Heart()
    draw(root, canvas, heart)
    root.mainloop()
