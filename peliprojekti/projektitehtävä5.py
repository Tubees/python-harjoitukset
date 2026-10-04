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

class esine:
    def __init__(self, nimi):
        self.nimi = nimi




def aloita(pelaaja):
    
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

        elif valinta == "0":
            tallenna_peli(pelaaja)
            lopeta()

        


def lopeta():
    print("Peli suljetaan")
    quit()



# Luodaan pelin esineet ja huoneet
taskulamppu = esine("Taskulamppu")

huone1 = huone("ranta", taskulamppu, "", None)
huone2 = huone("luola", None, "Etenit luolaan taskulampun avulla", "taskulamppu")
huone3 = huone("viidakko", None, "Saavuit metsään", None)
huone4 = huone("vuori", None, "Nousit vuorelle", "köysi")


#pelaaja = pelaaja(nimi, huone1)
    
#pohja tallentamiselle(vaihto json?)
def tallenna_peli(pelaaja):
    with open(f"peliprojekti/pelaajat/{pelaaja.nimi}.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(f"Nimi: {pelaaja.nimi}\n")
        tiedosto.write(f"Sijainti: {pelaaja.huone.nimi}\n")

        

    print("Peli tallennettu!")

#phja lataamiselle(vaihto json?)
def lataa_peli(nimi):
    with open(f"peliprojekti/pelaajat/{nimi}.txt", "r", encoding="utf-8") as tiedosto:
        teksti = tiedosto.read()
        hahmo = pelaaja(teksti[0], teksti[1])
        

    print("Peli ladattu!")
    return hahmo


def päävalikko():
    print("1. Uusi pelaaja")
    print("2. Lataa tallennus")
    print("3. Ohjeet")
    print("4. Lopeta")
    valinta = input("Valitse toiminto(1-2): ")
    if valinta == "1":
        nimi = input("Syötä nimi: ")
        ikä = int(input("Syötä ikä: "))
        if ikä < 12:
            print("peli kielletty alle 12-vuotiailta")
            lopeta()
        else:
            hahmo = pelaaja(nimi, huone1)
            aloita(hahmo)
            
    elif valinta == "2":
        nimi = input("Syötä nimi: ")
        hahmo = lataa_peli(nimi)
        aloita(hahmo)
    elif valinta == "3":
        
        with open("peliprojekti/ohjeet.txt", "r") as tiedosto:
            ohjeet = tiedosto.read()
            print(ohjeet)
        päävalikko()
        pass
    elif valinta == "4":
        lopeta()

päävalikko()


