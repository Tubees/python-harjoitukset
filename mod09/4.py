import random

class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
        
    def kulje(self, aika):
        if aika > 0:
            self.kuljettumatka += aika*self.nopeus



    
autot = []

for i in range(1, 11):
    huippunopeus = random.randint(100,200)
    auto = Auto(f"ABC-{i}", huippunopeus)
    print(auto.rekisteri)
    print(auto.huippunopeus)
    autot.append(auto)

voittaja = False
while not voittaja:

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

        if auto.kuljettumatka >= 10000:
            print(f"Auto {auto.rekisteri} voitti")
            voittaja = True
            break

for auto in autot:
    print(f"Auton rekisteritunnus {auto.rekisteri}, huippunopeus {auto.huippunopeus} ja kuljettu matka {auto.kuljettumatka} km")



