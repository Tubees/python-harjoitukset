class Hissi:
    def __init__(self, akerros, ykerros):
            self.akerros = akerros
            self.ykerros = ykerros 
            self.kerros = akerros

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



hissi = Hissi(0, 20)
hissi.siirry_kerrokseen(21)
hissi.siirry_kerrokseen(20)
print(hissi.kerros)
hissi.siirry_kerrokseen(0)
print(hissi.kerros)
