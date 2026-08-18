import random
rand = random.randint(1, 10)
while True:
    x = int(input("Luku: "))
    if x == rand:
        print("Oikein")
        break
    elif x > rand:
        print("Liian suuri arvaus")

    else:
        print("Liian pieni arvaus")