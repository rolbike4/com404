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

life = 7

correct_answer = 0
incorrect_answer = 0
q1 = input()

#
if (q1 == "a"):
    print("Correct you gained a life")
    life += 1
    correct_answer += 1
    if (life >= 6):
        life = 6
    print("Life","♥"*life)

else:
    print("Incorrect you lost a life")
    incorrect_answer -= 1
    life -= 1
    print("Life","♥"*life)
if  (life == 0):
    print("You lost, good luck next time!")