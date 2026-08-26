import random

def noppa():
    return random.randint(1, 6)

while True:
    nop = noppa()
    print(nop)
    if nop == 6:
        break

