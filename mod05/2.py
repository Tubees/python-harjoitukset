list = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        list.sort(reverse=True)
        print(list[:5])
        break
    luku = float(luku)
    list.append(luku)