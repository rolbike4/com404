print("What phrase do you see?")

phrase = str(input())
reverse =""

for letters in range (len(phrase)-1,-1,-1):
    letter = phrase[letters]
    reverse += letter
print(reverse)