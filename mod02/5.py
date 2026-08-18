leiviskä = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

naula += leiviskä * 20
luoti += naula * 32

g = luoti * 13.3
kg = g // 1000
g = round(g % 1000, 2)


print("Massa nykymittojen mukaan: " + str(kg) + " kilogrammaa ja " + str(g) + " grammaa")
