pienin = None
suurin = None
luku = None

while True:
    
    luku = input("Luku: ")
    if luku == "":
        print("Tyhjä")
        print("suurin " + str(suurin))
        print("pienin " + str(pienin))
        break
    luku = float(luku)
    if suurin is None or luku > suurin:
        suurin = luku
    if pienin is None or luku < pienin:
        pienin = luku
    