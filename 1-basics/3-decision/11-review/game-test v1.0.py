print("""Hello to my quizz game

For every right answer you get to the next question ....

but for every wrong one you lose one health

You start with 3 lives (that look like these ♥) but you can go up to 6 if you answer corectly the questions

if you lose are your lifes you go back to the begininGOOD LUCK
""")

print("Please enter your name")
name = input()
print("Nice to meet you",name)

print("Okay lets begin... , btw after every question you will be able to see your health... have fun!")
print("health been set to ♥♥♥")

print("Question 1: whats the talests buildin in the world ?")

life = 3
correct_answer = 0
incorrect_answer = 0
q1 = input()

#
if (q1 == "Burj Khalifa"):
    print("Correct you gained a life")
    life += 1
    correct_answer += 1
    if (life >= 6 ):
        life = 6
        print("Life","♥"*life)
else:
    print("Incorrect you lost a life")
    incorrect_answer -= 1
    life -= 1
    print("Life","♥"*life)

if  (life == 0):
    print("You lost, good luck next time!")
#
print("Question 2: What is the fastest car in the world")
q2 = input()
if (q2 == "Koenigsegg Agera RS"):
    print("Correct you gained a life")
    life+1
    correct_answer =+ 1
else:
    print("Incorrect you lost a life")
    incorrect_answer -= 1
    life -= 1
    print("Life","♥"*life)

if  (life == 0):
    print("You lost, good luck next time!")
    exit()
#
print("Question 3:What is the 3rd planet from the sun")
q3 = input()
if (q3 == "Earth"):
    #print("Correct you gained a life")
    life >= 6
    life = life
    print("Life","♥"*life)
    life += 1
    correct_answer =+ 1
else:
    life -= 1
    incorrect_answer -= 1
    print("Incorrect, you lost a life")
    if (life == 0):
        life = 0

        print("You lost all your lifes, good luck next time!")
        exit()
    else:
        print("Life","♥"*life)

#
print("Question 4:What is the biggest American Phone Company?")
q4 = input()
if (q4 == "Apple"):
    print("Correct you gained a life")
    correct_answer =+ 1
    life += 1
    if (life >= 6 ):
        life = 6
        print("Life","♥"*life)
else:
    life -= 1
    incorrect_answer -= 1
    print("Incorrect, you lost a life")
    if (life == 0):
        life = 0
        print("You lost all your lifes, good luck next time!")
        exit()
    else:
        print("Life","♥"*life)

#
print("Question 5:How many hearths does an octopus have")
q5 = input()
if (q5 == "3"):
    print("Correct you gained a life")
    correct_answer =+ 1
    life += 1
    if (life >= 6 ):
        life = 6
        print("Life","♥"*life)
else:
    life -= 1
    incorrect_answer -= 1
    print("Incorrect, you lost a life")
    if (life == 0):
        life = 0
        print("You lost all your lifes, good luck next time!")
        exit()
    else:
        print("Life","♥"*life)

#

print("You won,",name, "with",correct_answer,"answers and",incorrect_answers,"answers")