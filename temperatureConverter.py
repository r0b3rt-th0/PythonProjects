#Convert fahrenheit to celsius 
import random, temperatureConverter
from colorama import Fore

red = Fore.RED
black = Fore.BLACK
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE

def temperatureConverter(user_input):
    FAHRENHEIT_TO_CELSIUS = (user_input - 32) * 5/9 

    if(user_input >= 90):
        print("Fahrenheit:  ", red, user_input, black)
        print("Celsius: ", red, FAHRENHEIT_TO_CELSIUS, black)
    elif(user_input >= 75) & (user_input <= 89):
        print("Fahrenheit:  ", yellow, user_input, black)
        print("Celsius: ", yellow, FAHRENHEIT_TO_CELSIUS, black)
    elif(user_input >= 64) & (user_input <= 74):
        print("Fahrenheit:  ", green, user_input, black)
        print("Celsius: ", green, FAHRENHEIT_TO_CELSIUS, black)
    else:
        print("Fahrenheit:  ", blue, user_input, black)
        print("Celsius: ",  blue, FAHRENHEIT_TO_CELSIUS, black)

user=int(input("Enter a temperature in Fahrenheit to conver to Celsius: "))

for x in range(5):
    temperatureConverter(user) 
    user=float(input("Enter a temperature in Fahrenheit to conert to celsius: "))