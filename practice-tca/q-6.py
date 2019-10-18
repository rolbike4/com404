def is_slow_zombie(zombie_speed):
    if (zombie_speed < 5):
        return True
    else:
        return False



def take_action(zombie_mutation,zombie_nfs):
    if is_slow_zombie(zombie_nfs):
        return "This",zombie_mutation,"zombie is a slow zombie. You can run around it!"
    else:
         "This",zombie_mutation, ",zombie is a fast zombie. You better hide!"


def run():
    print("What type of mutation?")
    mutation_type = input()
    print("What speed does thje zombie have?")
    zombie_speed = int(input())
    print("Do you want to identify or action?")
    user_answer = input()
    if (user_answer == "identify"):
        print("A slow zombie:",is_slow_zombie(zombie_speed))
    elif(user_answer == "action"):
        print(take_action(mutation_type,zombie_speed))
    else:
        print("MUE")


run()
