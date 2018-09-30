getal = int(input("Geef een getal: "))

while getal > -1:
    if getal == 0:
        print(getal)
        getal -= 1
    else:
        print(getal, end=" .. ")
        getal -= 1

