def sum_weights(bop_weight,beep_weight):
    total_weight = bop_weight + beep_weight
    return total_weight

def calc_avg_weight(bop_weight,beep_weight):
    avg_weight = (bop_weight + beep_weight) / 2
    return avg_weight

def run():
    print("Enters Bop's weight")
    bop_weight = int(input())
    print("Enters Beep's weight")
    beep_weight = int(input())
    print("Do you want the sum or average?")
    word = input()
    if (word == "sum"):
        answer= sum_weights(bop_weight,beep_weight)
        print(answer)
    else:
        (word == "average")
        answer = calc_avg_weight(bop_weight,beep_weight)
        print(answer)

run()
