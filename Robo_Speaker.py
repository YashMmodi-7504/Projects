

import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to RoboSpeaker 1.1 Created by Yash Modi")
    while True:
        x = input("Enter what do you want me to speak: ")
        if x.lower() == "q":
            engine.say('bye bye friend')
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()

