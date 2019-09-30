print("What is your name human?")
name = input()
print("How old are you?",name)
age = int(input())
print("How tall are you?",name)
height = float(input())
print("What is your wheight?",name)
weight = float(input())

heightsquared = height*height

bodymass = weight/heightsquared

print(name,"your age is",age,"and your bmi is",bodymass)