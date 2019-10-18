def program():
    print("please enter a word")
    word = input()

    print("Please select an option")
    print("""
    1.Display in a Box
    2.Display Lower-case
    3.Display Upper-case
    4.Display Mirrored
    5.Repeat
    """)

    option = int(input())

    if (option == 1):
        word_box(word)
    elif(option == 2):
        lower_case(word)
    elif(option == 3):
        upper_case(word)
    elif(option == 4):
        mirrored(word)
    elif(option == 5):
        repeat(word)
def word_box(word):
    print("*" * (len(word) + 10))
    print("*      ", word, "*")
    print("*" * (len(word) + 10))

def lower_case(word):
    print(word.lower())

def upper_case(word):
    print(word.upper())

def mirrored(word):
    reverse = ""
    for letter in word:
        reverse = letter + reverse
    print(reverse)

def repeat(word):
    print("How many times should i print the word")
    word_repeat = int(input())
    for number in range (0,word_repeat,1):
        if (number % 2 == 0):
            lower_case(word)
        else:
            upper_case(word)



program()