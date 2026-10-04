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
            auto1.kuljettumatka += aika*self.nopeus



    

auto1 = Auto("ABC-123", 142)

print(auto1.rekisteri)
print(auto1.huippunopeus)
print(auto1.nopeus)
print(auto1.kuljettumatka)

auto1.kiihdytä(200)
auto1.kulje(4.5)
print(auto1.kuljettumatka)



