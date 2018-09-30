getal1 = int(input("Getal 1: "))
getal2 = int(input("Getal 2: "))
getal3 = int(input("Getal 3: "))

if getal1 == getal2 + getal3 or getal2 == getal1 + getal3 or getal3 == getal1 + getal2:
    print("dit lukt")
else:
    print("dit lukt niet")