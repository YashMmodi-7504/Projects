import requests
import json
import pyttsx3

city = input("Enter the name of the city:\n")

url = f"https://api.weatherapi.com/v1/current.json?key=bff97955f45e478db1c50609241006&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
temp_c = wdic["current"]["temp_c"]
print(f"The current temperature in {city} is {temp_c} degrees Celsius.")

engine = pyttsx3.init()
engine.say(f'The current weather in {city} is {temp_c} degrees Celsius.')
engine.runAndWait()
