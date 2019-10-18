print("How many days remain until the next full moon?")
user_response_number = int(input())
print("We must count the days...")

number_countdown = 0

#while (user_response_number > number_countdown):
    #print("The full moon will be upon us in",user_response_number, "days.")
    #user_response_number = user_response_number - 1
#print( "It's a full moon. The beast has been unleashed!\nMay it have mercy on our souls.")

for number in range (user_response_number,0,-1):
    print("The full moon will be upon us in",number, "days.")
print( "It's a full moon. The beast has been unleashed!\nMay it have mercy on our souls.")
