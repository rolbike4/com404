def is_league_united(hero1,hero2):
    if hero1 == "superman" and hero2 == "wonderwoman" or hero1 == "wonderwoman" and hero2 == "superman":
        return True
    else:
        return False


def decide_plan(hero1,hero2):
    if is_league_united(hero1,hero2) is True:
        return "Time to save the world!"
    else:
        return "We must unite the league!"

def run():
    superman = input("Please enter the first hero name\n")
    wonderwoman = input("Please enter the seccond hero name\n")
    user_input = input("League or Plan?\n")
    if user_input == "league":
        print(is_league_united(superman,wonderwoman))
    elif(user_input == "plan"):
        print(decide_plan(superman,wonderwoman))
    else:
        print("Invalid command. Please try again")

run()