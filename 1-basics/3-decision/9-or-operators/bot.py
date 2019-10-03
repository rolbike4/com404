print("What type of adventure you like")
user_answer = input()
if ((user_answer == "scary") or (user_answer == "short")):
    print("Entering the dark forest")
elif ((user_answer == "safe") or (user_answer == "long")):
        print("Taking the safe route!")
else:
    print("Not sure which route to take.")
