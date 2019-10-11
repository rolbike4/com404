print("What phrase do you see?")

phrase = str(input())
reverse = ""
for letter in phrase:
    print(letter)
    reverse = letter + reverse
print(reverse)