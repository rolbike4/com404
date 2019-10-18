def cross_bridge(steps):

    step = 0

    while (step < steps):
        print("Crossed Step")
        step = step + 1

    if (steps > 5):
        print("The bridge is collapsing")
    else:
        print("We must keep going")


cross_bridge(3)
cross_bridge(6)