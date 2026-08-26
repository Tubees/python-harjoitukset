import random

kuutiot = int(input("Anna luku: "))
sum = 0

for i in range(1, kuutiot + 1 ):
    x = random.randint(1, 6)
    print("Kuutio " + str(i) + " on: " + str(x))
    sum += x

print("Summa on : " + str(sum))