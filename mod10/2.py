class Hissi:
    def __init__(self, akerros, ykerros, nro):
            self.akerros = akerros
            self.ykerros = ykerros 
            self.kerros = akerros
            self.nro = nro

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ykerros or kerros < self.akerros:
            print("kerros ei ole olemassa")
            return
        while self.kerros != kerros:
            if self.kerros < kerros:
                self.kerros_ylös()
            elif self.kerros > kerros:
                self.kerros_alas()


    def kerros_ylös(self):
        self.kerros += 1


    def kerros_alas(self):
        self.kerros -= 1


class Talo:
    def __init__(self, akerros, ykerros, hissit):
        self.hissit = []
        for i in range(hissit):
            self.hissit.append(Hissi(akerros, ykerros, i+1))

    def aja_hissiä(self, nro, kerros):
        for i in self.hissit:
            if i.nro == nro:
                i.siirry_kerrokseen(kerros)
                return
        print("Hissiä ei löytynyt")



talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 10)
talo.aja_hissiä(2, 3)
talo.aja_hissiä(3, -3)


for hissi in talo.hissit:
    print(f"Hissi {hissi.nro}, kerros {hissi.kerros}")

