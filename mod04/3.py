sukupuoli = input("Anna sukupuoli (mies/nainen): ")
hg = float(input("Hemoglobiini: "))
if sukupuoli == "nainen":
    if hg < 117:
        print("hemoglobiini alhainen")
    elif hg > 175:
        print("hemoglobiini korkea")
    else:
        print("hemoglobiini normaali")
elif sukupuoli == "mies":
    if hg < 134:
        print("hemoglobiini alhainen")
    elif hg > 195:
        print("hemoglobiini korkea")
    else:
        print("hemoglobiini normaali")
else:
    print("?")