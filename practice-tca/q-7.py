def under(msg):
    return "Halloween\n"+str(len(msg)*"-")+"\n"+msg

def over(draven):
    return draven+"\n"+ str(len(draven)*"-")+"\n""Halloween"

def both(both):
    return both+"\n"+ str(len(both)*"-")+"\n""Halloween"+"\n"+str(len(both)*"-")+"\n" +both

def grid(metin):
    x = min(len(metin)-1,4)
    for e in range(0,min(5,len(metin))):
        print("Halloween ","| Halloween"*x)






def run ():
    message = input("Enter a message: ")
    user_response = input("Enter an option: ")
    if (user_response == "under"):
        print(under(message))
    elif user_response =="over":
        print(over(message))
    elif user_response == "both":
        print(both(message))
    else:
        user_response == "grid"
        print(grid(message))
run()
print("1")