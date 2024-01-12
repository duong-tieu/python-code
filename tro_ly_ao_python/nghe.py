import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:   
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic) 
try :
    you = robot_ear.recognize_google(audio) 
except:
    you = ""     
print("You :" + you) # type: ignore


# import speech_recognition

# robot_ear = speech_recognition.Recognizer()

# with speech_recognition.Microphone() as mic:
#     try:
#         print("Robot: I'm listening")
#         audio = robot_ear.listen(mic, timeout=5)  # Set a timeout to avoid waiting indefinitely
#         print("Robot: I stopped listening")
        
#         # Using Google's speech recognition service
#         you = robot_ear.recognize_google(audio)
#         print("You said:", you)

#     except speech_recognition.WaitTimeoutError:
#         print("Robot: It took too long to capture audio. Please try again.")

#     except speech_recognition.UnknownValueError:
#         print("Robot: Sorry, I could not understand the audio. Please try again.")

#     except speech_recognition.RequestError as e:
#         print(f"Robot: There was an error with the speech recognition service: {e}")
