user_response_number = int(input("How many miles must I travel before I reach the secret base?\n"))

number_reverse = 0
print("I will count the miles....\n")
while (user_response_number > number_reverse):
    print( "I have",user_response_number,"miles to go before I reach the base")
    user_response_number = user_response_number - 1
print("I have arrived at the secret headquarters of the MIB!")
