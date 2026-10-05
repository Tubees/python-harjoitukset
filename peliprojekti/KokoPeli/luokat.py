class pelaaja:
    def __init__(self, nimi, huone):
        self.nimi = nimi
        self.huone = huone
        self.esineet = []
        self.max_esineet = 3
        self.pisteet = 0
        

    def liiku(self, kohde):

        self.huone = kohde


    def keraa_esine(self, esine):
        if len(self.esineet) <= self.max_esineet:
            self.esineet.append(esine)
            self.huone.esineet.remove(esine)
        else:
            print("Et voi kerätä enempää esineitä, pudota jokin esine ensin.")

    def pudota_esine(self, esine):
        #esine on indeksi listassa
        print(f"Pudotit esineen: {self.esineet[esine-1].nimi}")
        self.pelaaja.huone.esineet.append(self.esneet[esine-1])
        self.esineet.pop(esine-1)


class huone:
    def __init__(self, nimi, siirtymä_teksti, vaadittu_esine, vaatimus_teksti, roskat):
        self.nimi = nimi
        self.esineet = []
        self.siirtymä_teksti = siirtymä_teksti
        self.vaadittu_esine = vaadittu_esine
        self.huoneet = {}
        self.vaatimus_teksti = vaatimus_teksti
        self.roskat = roskat


    def lisaa_huone(self, huone):
        self.huoneet[len(self.huoneet) + 1] = huone



class esine:
    def __init__(self, nimi):
        self.nimi = nimi

