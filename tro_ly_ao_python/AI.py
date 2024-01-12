from ast import While
import speech_recognition
import pyttsx3
from datetime import date, datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:   
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic) 
            
    print("Robot ...")    
    try:
        you = robot_ear.recognize_google(audio) 
    except:
        you = ""     
    print("You: " + you)  # type: ignore 

    # Phần robot nghe
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hi Thien Phu"
    elif  "today" in you:
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        robot_brain = "Today is: " + d2
    elif  "time" in you:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")    
        robot_brain = "It's time: " + current_time
    elif "are" in you:
        robot_brain = "I'm fine thank you and you"    
    elif "again" in you :
        robot_brain = "Bye"
        break  # Exit the loop when saying goodbye
    else:
        robot_brain = "See you later"    

    print("Robot: " + robot_brain)              
    # phần robot hiểu

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    # phần robot nói
