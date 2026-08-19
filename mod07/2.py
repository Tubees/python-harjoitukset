nimet = set()

while True:
    nimi = input("Nimi? ")
    if nimi == "":
        print(nimet)
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print("Uusi nimi")