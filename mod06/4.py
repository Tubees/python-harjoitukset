import random

lsita = []

def listsum(x: list):
    return sum(x)

montako = int(input("montako lukua:"))
max = int(input("max: "))

for i in range(montako):
    lsita.append(random.randint(1, max))

summa = listsum(lsita)

print("Summa on " + str(summa))