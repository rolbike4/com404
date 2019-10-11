print("What level of brightness is required?")

required_brightness = int(input())

for brightness in range (2,required_brightness+1, 2):
    print("Adjusting brightness")

    print("Beep's brightness level:","*"*brightness)
    print("Bop's brightness level:","*"*brightness)
