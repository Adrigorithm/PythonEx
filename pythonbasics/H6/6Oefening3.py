def druk_vierkant(aantal, teken):
    for count in range(0, aantal):
        print(teken * aantal)

while True:
    teken = input("Geef het teken waarmee de lijnen gevormd worden (enter = stop): ")
    if teken == "":
        break
    aantal = int(input("Aantal tekens per lijn en aantal lijnen: "))
    druk_vierkant(aantal, teken)