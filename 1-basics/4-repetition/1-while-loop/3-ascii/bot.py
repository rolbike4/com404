#print message
print("How many bars should i charge?")
#user input
bars_to_charge = int(input())
#iteration
bars_charged = 0
#loop
while (bars_charged < bars_to_charge):
    bars_charged = bars_charged + 1
    print("Charging", "█" * bars_charged)
