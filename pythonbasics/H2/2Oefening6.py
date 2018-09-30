getal1 = int(input("Geef het eerste getal: "))
getal2 = int(input("Geef het tweede getal: "))


if getal1 == getal2:
    print("Het antwoord voor de getallen", getal1, "en", getal2, "= 0")
elif getal1 % 5 == 0 and getal2 % 5 == 0:
    print("Het antwoord voor de getallen", getal1, "en", getal2, "=", min(getal1,getal2))
else:
    print("Het antwoord voor de getallen", getal1, "en", getal2, "=", max(getal1,getal2))
