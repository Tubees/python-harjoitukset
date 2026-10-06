class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class kirja(julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä


    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumäärä}")

class lehti(julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.päätoimittaja}")




lehti1 = lehti("Aku ankka", "Aki Hyyppä")
lehti1.tulosta_tiedot()

kirja1 = kirja("Hytti n:o 6", "Rosa Liksom", 200)
kirja1.tulosta_tiedot()