dead_ends = 0
number_of_mummies = 0
loop_runs = 0
print("Escaping the tomb...\n")

for number in range (0,4,1):
    print("What lies before me?")
    user_response = input()
    if (user_response == "a dead end"):
        dead_ends = dead_ends +1
        print("Time to turn back")
    elif(user_response == "a mummy"):
        number_of_mummies = number_of_mummies + 1
        print("Better find another way")
    else:
        print("Let's move around it")

print("Encountered ",dead_ends," dead ends and",number_of_mummies, "mummies")