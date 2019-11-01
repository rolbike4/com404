def is_piatra_drop(item1,item2):
    if item1 =="fms" and item2 == "rib" or item1 == "rib" or item2 == "fms":
        return True
    else:
        return False

def decide_drop(item1,item2):
    if is_piatra_drop(item1,item2) is True:
        return "A picat ba"
    else:
        "Bagami-as"

def run():
    fms = input("Ce vrei prima arma\n")
    rib = input("Ce vrei ba la a doua\n")
    user_input = input("nob sau pro?\n")
    if user_input == "nob":
        print(is_piatra_drop(fms,rib))
    elif user_input == "pro":
        print(decide_drop(fms,rib))
    else:
        print("O fut pe ma-ta")


run()
