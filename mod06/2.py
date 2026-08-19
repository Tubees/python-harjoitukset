import random


tahkot = int(input("tahkot: "))

def noppa(max):
    return random.randint(1, max)


while True:
    heitto  = noppa(tahkot)
    print(heitto)
    if heitto == tahkot:
        break