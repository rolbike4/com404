#print message
print("how many live cables i need to avoid?")
#user input
live_cables_avoid = int(input())
#iteration
live_cables = 0
#loop
while (live_cables < live_cables_avoid):
    live_cables = live_cables + 1
    print("Avoiding...Done!",live_cables,"live cables avoided")

print("All live cables have now been avoided")