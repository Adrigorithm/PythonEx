getal1 = int(input("Getal 1 (0, 1 of 2): "))
getal2 = int(input("Getal 2 (0, 1 of 2): "))
getal3 = int(input("Getal 3 (0, 1 of 2): "))
if getal1 == getal2 == getal3:
    if getal1 != 2:
        print("5")
    else:
        print("10")
elif getal1 != getal2 and getal1 != getal3:
    print("1")
else:
    print("0")