print("Please enter a sequence of characters consisting of dashes and two markers e.g. X----X. ")
sequence = input()
print("Please enter the character for a marker")
marker = input()

marker_one_position = -1


for position in range(0,len(sequence),0):
    letter = sequence[position]
    if letter == marker:
        if marker_one_position == -1:
            marker_one_position = position
        else:
                marker_one_position = position




