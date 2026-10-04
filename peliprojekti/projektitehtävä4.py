class pelaaja:
    def __init__(self, nimi, huone):
        self.nimi = nimi
        self.esineet = []
        self.huone = huone

    def liiku(self, kohde):

        self.huone = kohde
        print(f"Uusi sijainti: {self.huone.nimi}")


    def keraa_esine(self, esine):
        self.esineet.append(esine)
        print(f"Kerätty esine: {esine}")
    

class huone:
    def __init__(self, nimi, esine, siirtymä_teksti, vaadittu_esine):
        self.nimi = nimi
        self.esine = esine
        self.siirtymä = siirtymä_teksti
        vaadittu_esine = vaadittu_esine


    def nayta_tiedot(self):
        print(f"Huone: {self.nimi}")
        print(f"Esine: {self.esine}")




class esine:
    def __init__(self, nimi):
        self.nimi = nimi




def aloita():
    print("\nPeli alkaa")
    while True: 
        print("Toiminnot:")
        print("1. Tutki huonetta")
        print("2. kerää esine")
        print("3. Siirry huoneeseen")
        print("0. Lopeta peli")

        valinta = input("Valitse toiminto: ")
        if valinta == "1":
            print(f"olet huoneessa: {pelaaja.huone.nimi}")
            print(f"Huoneessa oleva esine: {pelaaja.huone.esine.nimi}")

        elif valinta == "2":

            pelaaja.keraa_esine(pelaaja.huone.esine)
            print(f"Keräsit esineen: {pelaaja.huone.esine.nimi}")
            pelaaja.huone.esine = None

        elif valinta == "3":
            pelaaja.liiku(huone2)
            print(f"Siirryit huoneeseen: {pelaaja.huone.nimi}")

        


def lopeta():
    print("Peli suljetaan")
    quit()





nimi = input("Syötä nimi: ")
ikä = int(input("Syötä ikä: "))


# Luodaan pelin esineet ja huoneet
taskulamppu = esine("Taskulamppu")

huone1 = huone("ranta", taskulamppu, "", None)
huone2 = huone("luola", None, "Etenit luolaan taskulampun avulla", "taskulamppu")
huone3 = huone("viidakko", None, "Saavuit metsään", None)
huone4 = huone("vuori", None, "Nousit vuorelle", "köysi")


pelaaja = pelaaja(nimi, huone1)
    






    







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
            pass
        elif valinta == "3":
            lopeta()






