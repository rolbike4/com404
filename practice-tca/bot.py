def abc(x):
    if x==0:
        return 0
    return x+abc(x-1)
while True:
    n=int(input("n: "))
    print("suma primelor n cifre este : ",abc(n))