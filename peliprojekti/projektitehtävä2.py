
#!!Peli toimmii syöttämällä komentoriviin numeroita tai 'lopeta' pelin sulkemiseksi!!

nimi = input("Syötä nimi: ")
ikä = int(input("Syötä ikä: "))

if ikä < 12:
    print("Peli kielletty alaikäisiltä. Peli suljetaan...")
    quit()
else:
    while True:
        print("\nHei " + nimi + "!\n1. Aloita Peli\n2. Asetukset\n")
        valinta = input("Valitse toiminto(1-2) tai syötä 'lopeta': ")
        if valinta == "1":
            print("\nPeli alkaa")
        elif valinta == "2":
            print("\nAsetukset avataan")
        elif valinta == "lopeta":
            print ("Peli suljetaan")
            quit()