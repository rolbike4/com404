print("Where should i look")

user_answer_room = input()

if (user_answer_room == "in the bedroom"):
    print("Where in the bedroom should i look?")
    user_answer_room_specific_1 = input()
    if (user_answer_room_specific_1== "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
elif (user_answer_room == "in the bathroom"):
    print("Where in the bathroom should I look?")
    user_answer_room_specific_2 = input()
    if(user_answer_room_specific_2 == "in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery")
elif (user_answer_room == "in the lab"):
    print("Where in the lab should i look?")
    user_answer_room_specific_3 = input()
    if(user_answer_room_specific_3 == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")
else:
    print("I do not know where that is but I will keep looking")




