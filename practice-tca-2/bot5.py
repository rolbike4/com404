user_response = int(input("How many zones must I cross?\n"))

print("Crossing zones...")

zones = 0

while (zones<user_response):
    print("…crossed zone",user_response)
    user_response = user_response - 1
print("Crossed all zones.  Jumanji!")