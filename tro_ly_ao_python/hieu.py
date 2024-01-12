# you = "hello"

# if you == "":
#     robot_brain = "I can't hear you, try again"
# elif you == "hello":
#     robot_brain = "Hi Thien Phu"
# elif you == "Today":
#     robot_brain = "Wenedsday" 
# else:
#     robot_brain = "I'm fine thank you and you"    
    
# print(robot_brain)      


from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)        