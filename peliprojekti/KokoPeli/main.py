from luokat import pelaaja, huone, esine
import json
import random

uusi_peli = True
#Funktiot
#lopeta peli
def lopeta(pelaaja):
    #tallenna peli ennen lopettamista
    tallenna_peli(pelaaja)
    print("Peli suljetaan")
    quit()

#sulje peli tallentamatta
def loppu():

    print("Onneksi olkoon! Läpäisit pelin.")
    quit()



#Tallennetaan peli json muodossa
def tallenna_peli(pelaaja):
    tiedot = {
        "nimi": pelaaja.nimi,
        "sijainti": pelaaja.huone.nimi,
        "esineet": [esine.nimi for esine in pelaaja.esineet],
        "pisteet": pelaaja.pisteet 
    }
    with open(f"peliprojekti/kokopeli/pelaajat/{pelaaja.nimi}.json", "w", encoding="utf-8") as tiedosto:
        json.dump(tiedot, tiedosto)
    print("Peli tallennettu!")


#lataa käyttäjän tallennus
def lataa_peli(nimi):
    global uusi_peli
    hahmo = None
    try:
        with open(f"peliprojekti/kokopeli/pelaajat/{nimi}.json", "r", encoding="utf-8") as tiedosto:
            tiedot = json.load(tiedosto)
            hahmo = pelaaja(tiedot["nimi"], tiedot["sijainti"])
            hahmo.pisteet = tiedot["pisteet"]

            #Etsitään oikea huone ja lisätään se pelaajalle
            for x in huoneet:
                if x.nimi == tiedot["sijainti"]:
                    hahmo.huone = x

            #Käydään esineet läpi. lisätään ne pelaajalle ja poistetaan huoneesta
            for x in tiedot["esineet"]:
                for i in huone1.esineet:
                    if i.nimi == x:
                        hahmo.esineet.append(i)
                        huone1.esineet.remove(i)

            print("Peli ladattu!")
            uusi_peli = False
            return hahmo


    except FileNotFoundError:
        return hahmo                   






#Valmis?
#päävalikko
def päävalikko():
        while True:
            print("1. Uusi pelaaja")
            print("2. Lataa tallennus")
            print("9. Lopeta")
            valinta = input("Valitse toiminto(1-9): ")
            if valinta == "1":
                nimi = input("Syötä nimi: ")
                ikä = int(input("Syötä ikä: "))
                if ikä < 12:
                    print("peli kielletty alle 12-vuotiailta")
                    print("Peli suljetaan")
                    quit()
                else:
                    hahmo = pelaaja(nimi, huone1)
                    aloita(hahmo)
                    
            elif valinta == "2":
                nimi = input("Syötä nimi: ")
                hahmo = lataa_peli(nimi)
                aloita(hahmo)

            elif valinta == "9":
                quit()


def valinnat():
    print("\n"*100)
    print("\nToiminnot:")
    print("1. Tutki huonetta")
    print("2. kerää esine")
    print("3. Pudota esine")
    print("4. Siirry huoneeseen")
    print("5. Kerää roska")
    print("6. Näytä esineet ja pisteet")
    print("7. Ohjeet")
    print("9. Lopeta peli")
    print("\n"*2)


#Siisti ja selkeä päälooppi
#Pää looppi
def aloita(pelaaja):
    valinnat()

    if uusi_peli == True:
        print("Haaksirikkouduit saarelle! Ympärrilläsi on erinlaisia esineitä.")
        print("Tehtäväsi on löytää pois saarrelta esineiden avulla. Voit kantaa vain 3 esinettä.")
        print("Huomaat että saarelle on ajautunut myös roskaa. ")
        print("Kerää roskat saadaksesi pisteitä")    
    else:
        print(f"Jatkat peliä huoneesta {pelaaja.huone.nimi}")

    while True: 
        print("\n"*1)
        valinta = input("Valitse toiminto: ")   

        #Tulosta huoneen nimi, esineet ja roskat
        if valinta == "1":
            valinnat()
            esineet = []
            huoneet = []
            for x in pelaaja.huone.esineet:
                esineet.append(x.nimi)
            print(f"Olet huoneessa {pelaaja.huone.nimi}, roskat: {pelaaja.huone.roskat}, esineet: {esineet}")
            for x in pelaaja.huone.huoneet:
                huoneet.append(pelaaja.huone.huoneet[x].nimi)
            print(f"Seuraavat huoneet: {huoneet}")

        #kerää esine ja poista se huoneesta
        elif valinta == "2":

            i = 1
            for x in pelaaja.huone.esineet:
                print(f"{i}. {x.nimi}")
                i += 1
            valinta = int(input("Valitse esine: "))
            valinnat()
            pelaaja.keraa_esine(pelaaja.huone.esineet[valinta-1])



        #Pudota esine
        elif valinta == "3":
            i = 1
            for x in pelaaja.esineet:
                print(f"{i}. {x.nimi}")
                i += 1
            valinta = int(input("Valitse esine: "))
            valinnat()

            pelaaja.pudota_esine(pelaaja.esineet[valinta-1])
            

        #Siirry huoneeseen
        elif valinta == "4":
            print("Seuraavat huoneet:")
            for x in pelaaja.huone.huoneet:
                print(f"{x}. {pelaaja.huone.huoneet[x].nimi}")

            valinta = int(input("Mikä huone: "))
            huone = pelaaja.huone.huoneet[valinta]

            if huone.vaadittu_esine is None or huone.vaadittu_esine in pelaaja.esineet:
                if huone.nimi == "helikopteri":
                    loppu()
                else:
                    valinnat()
                    print(huone.siirtymä_teksti)
                    pelaaja.liiku(huone)
            else:
                valinnat()
                print(huone.vaatimus_teksti)

        #Kerää roska huoneesta 
        elif valinta == "5":
            valinnat()
            if pelaaja.huone.roskat > 0:
                pelaaja.huone.roskat -= 1
                pelaaja.pisteet += 1
                print("Keräsit roskan.")
                print(f"Pisteesi: {pelaaja.pisteet}")
            else:
                print("Huoneessa ei ole roskia.")
            
        #Näytä esineesi ja pisteesi
        elif valinta == "6":
            valinnat()
            esineet = []
            for i in pelaaja.esineet:
                esineet.append(i.nimi)
            print(f"Esineesi: {esineet}")
            print(f"Pisteesi: {pelaaja.pisteet}")
        elif valinta == "7":
            valinnat()
            with open("peliprojekti/KokoPeli/ohjeet.txt", "r", encoding="utf-8") as tiedosto:
                print(tiedosto.read())
            
        #sulje peli ja tallenna
        elif valinta == "9":
            
            lopeta(pelaaja)





#esineet
alkuesineet = []
taskulamppu = esine("Taskulamppu")
köysi = esine("Köysi")
veitsi = esine("Veitsi")
tikapuut = esine("tikapuut")
laskuvarjo = esine("Laskuvarjo")
bensa = esine("Bensa")
kumivene = esine("kumivene")

alkuesineet.append(taskulamppu)
alkuesineet.append(köysi)
alkuesineet.append(veitsi)
alkuesineet.append(tikapuut)
alkuesineet.append(laskuvarjo)
alkuesineet.append(bensa)
alkuesineet.append(kumivene)

#Luodaan kaikki huoneet
huone1 = huone("ranta", "Palasit rannalle", None, "", random.randint(1,3))
huone1.esineet = alkuesineet

huone2 = huone("luola",  "Etenit luolaan taskulampun avulla", taskulamppu, "Luolassa on pimeää, tarvitset esineen jolla voit nähdä." , random.randint(1,3))
huone5 = huone("rotko", "Ylitit rotkon köyden avulla", köysi, "Rotkon ylittämiseen tarvitset jotain mistä roikkua", random.randint(1,3))

huone3 = huone("viidakko" , "Etenet viidakossa veitsen avulla", veitsi, "Viidakko on tiheää, tarvitset jotain terävää reitin tekemiseen", random.randint(1,3))
huone6 = huone("joki", "Yliti joen kumiveneen avulla", kumivene, "Joessa on kova virtaus tarvitset jotain pysyäksesi pinalla", random.randint(1,3))

huone4 = huone("vuori", "Kiipesit vuorelle tikapuiden avulla", tikapuut, "Vuori on jysrkkä, tarvitset jotain millä pääset ylös", random.randint(1,3))
huone7 = huone("vesiputous", "Hypäsit vesiputouksen yli laskuvarjon avulla", laskuvarjo, "Tarvitset jotain millä pääset turvallisesti alas.", random.randint(1,3))

huone8 = huone("helikopteri", "Saavuit helikopterille", bensa, "Helikopterin käyttö vaatii bensaa.", None)

#siirtymät      
#Ensimäisestä huoneesta
huone1.lisaa_huone(huone2)
huone1.lisaa_huone(huone3)
huone1.lisaa_huone(huone4)

#Toisista huoneesta eteen ja taaksepäin
huone2.lisaa_huone(huone1)
huone2.lisaa_huone(huone5)
huone3.lisaa_huone(huone1)
huone3.lisaa_huone(huone6)
huone4.lisaa_huone(huone1)
huone4.lisaa_huone(huone7)

#kolmannesta huoneesta eteen ja taaksepäin
huone5.lisaa_huone(huone2)
huone5.lisaa_huone(huone8)
huone6.lisaa_huone(huone3)
huone6.lisaa_huone(huone8)
huone7.lisaa_huone(huone4)
huone7.lisaa_huone(huone8)
huoneet = [huone1, huone2, huone3, huone4, huone5, huone6, huone7, huone8]

#pelin aloitus
päävalikko()


