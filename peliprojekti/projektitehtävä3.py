nimi = input("Syötä nimi: ")
ikä = int(input("Syötä ikä: "))

lista = []

def aloita():
    print("\nPeli alkaa")
    print("\nLisää esineitä reppuun(Lopeta syötämällä tyhjä merkkijono)")
    while True:
        x = input("Syötä esine: ")
        lista.append(x)
        if x == "":
            break

def listaa():
    print("\nEsineet repussa:")
    for x in lista:
        print(x)

def lopeta():
    print("Peli suljetaan")
    quit()

if ikä < 12:
    print("Peli kielletty alaikäisiltä. Peli suljetaan...")
    quit()
else:
    while True:
        print("\nHei " + nimi + "!\n1. Aloita Peli\n2. Listaa esineet\n3. Lopeta")
        valinta = input("Valitse toiminto(1-3): ")
        if valinta == "1":
            aloita()
        elif valinta == "2":
            listaa()
        elif valinta == "3":
            lopeta()



