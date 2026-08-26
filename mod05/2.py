tuuma = float(2.54)
while True:
    luku = int(input("Anna luku: "))
    if luku <0:
        print("negatiiviinen luk")

        break 

    else: 
        print(str(luku )+ "tuumaa on : " + (str(luku * tuuma) + "cm"))
