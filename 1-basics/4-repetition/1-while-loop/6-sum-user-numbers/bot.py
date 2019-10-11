print("How many numbers should i add up")
number = int(input())

numbers_required = 0

stage = 0

number_total = 0
number_inserted = 0

while(numbers_required < number):
    stage = stage +1
    numbers_required = numbers_required + 1
    print("please enter a number",stage,"of",number)
    number_inserted = int(input())
    number_total = number_total + number_inserted


print(number_total)