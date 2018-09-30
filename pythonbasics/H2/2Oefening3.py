getal = int(input("Geef een getal: "))

if getal < 0:
    print("Negatieve getallen worden niet getest")
else:
    eindcijfer = int(input("Met welk eindcijfer wil je testen: "))
    if str(eindcijfer) == str(getal)[-1:]:
        print(getal, "eindigt inderdaad op", eindcijfer)
    else:
        print(getal, "eindigt niet op", eindcijfer)