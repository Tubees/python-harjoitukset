name = "python"
passw = "rules"
tries = 0

while tries < 5:
    nimi = input("Nimi: ")
    sala = input("Salasana: ")
    if nimi == name and sala == passw:
        print("Tervetuloa!")
        break
    tries += 1
    print("Yrityksiä: " + str(tries))

else: 
    print("pääsy evätty")