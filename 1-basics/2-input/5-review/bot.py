#1-Output printed message
print("Hello world")

#2- output multiple line of messages

print("""
    Hello world!
    this is a multi line message""")

#3- some special characters

print("\n Displays a new line")
print("\t Displays a tab space")
print("\\ Displays a back slash")
print("\" Displays a double quote")
print("\' Displays a single quote")

#4-Ascii art

print("##########")
print("#        #")
print("#        #")
print("##########")

#5- input
print("Whats your name human?")
name=input()
print("Nice to meet you",name)


#6- input ascii art

print("please enter a character for the left and right eye")

leye=input()
reye=input()

print("##########")
print("#"" ",leye, reye, "   ""#")
print("#        #")
print("##########")


#7 - BMI CALCULATOR

print("WHats your name human")
print ("Nice to meet you",name)
print("Whats your height in meters please")
height = float(input())
print("Whats your weight in kg please")
weight = int(input())
print("How old are you?")
age = float(input())


bmi = weight/(height*height)

print("Your BMI for your age,",age,",is",bmi)


#8 - Beep shiled and life level

print("please enter the level of health")
health = int(input())
print("please enter the level of shield")
shield = int(input())

print("thank you my health and shiled levels has been restored")

print("Lives:","♥"*health)
print("Health", "♥"*shield)
