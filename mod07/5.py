import random

lsita = []


def listpari(x: list):
    new = []
    for i in x:
        if i % 2 == 0:
            new.append(i)
    return new

montako = int(input("montako lukua:"))
max = int(input("max: "))

for i in range(montako):
    lsita.append(random.randint(1, max))

uusilista = listpari(lsita)

print(lsita)
print(uusilista)