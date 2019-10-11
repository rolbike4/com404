print("What strange markings do you see?")

user_word = input()
print("Identifying...")

index = 0

for position in range(0, len(user_word), 1):
    print("Index",index,user_word[position])
    index = index + 1

