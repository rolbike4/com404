value = 100

print("Your health is 100%. Escape is in progress...")

timer_1 = 0
timer_2 = 5

for number in range (timer_1<timer_2):
    user_response = input("Who is that?\n")
    if (user_response == "Smiler's Bot"):
        value = value -20
        print("Time to jam out of here!")
    elif (user_response == "hacker"):
        value = value + 20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")

    timer_2 = timer_2 -1
print("Escaped! Health is "+str(value)+"%")