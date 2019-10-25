from bot10 import under,over,grid,both

user_input = input("Please enter a word\n")

user_option = int(input("Pick 1,2,3,4\n"))

if user_option == 1:
    print(under(user_input))
elif user_option == 2:
    print(over(user_input))
elif user_option == 3:
    print(both(user_input))
elif user_option == 4:
    a = print
    n = int(input("Enter grid size\n"))
    a(grid(user_input,n))