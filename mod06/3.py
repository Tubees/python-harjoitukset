luku = int(input("Luku:"))
if luku < 2:
    print("Luku ei ole alkuluku")
else:
    for i in range(1, luku + 1):
        if luku % i == 0 and i != 1 and i != luku:

            print("Luku ei ole alkuluku")
            break
    else:
        print("Luku on alkuluku")