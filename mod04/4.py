vuosi = int(input("Anna vuosi: "))


if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("karkausvuosi")
        else:
            print("ei ole")
    else:
        print("karkausvuosi")
else:
    print("ei ole")