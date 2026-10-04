class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    

auto1 = Auto("ABC-123", 142)

print(auto1.rekisteri)
print(auto1.huippunopeus)
print(auto1.nopeus)
print(auto1.kuljettumatka)