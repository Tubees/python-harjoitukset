def gtol(g):
    return 3.785 * g

while True:
    g = float(input("Galonia: "))
    if g < 0:
        break
    print(gtol(g))
