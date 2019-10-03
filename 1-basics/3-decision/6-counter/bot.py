

print("Please enter the first number")

first_number = int(input())

print("Please enter the seccond number")

seccond_number = int(input())

print("Please enter the third number")

third_number = int(input())

even_counter = 0
odd_counter = 0
if (first_number % 2 == 0):
    even_counter += 1
else:
    odd_counter +=1


if (seccond_number % 2 == 0):
    even_counter += 1
else:
    odd_counter +=1


if (third_number % 2 == 0):
    even_counter +=1
else:
    odd_counter +=1

print("There were",even_counter,"even numbers and",odd_counter,"odd numbers")
