import random
spreekwoorden = ["de aanhouder wint", "wie a zegt moet ook b zeggen", "onkruid vergaat niet", "oost west thuis best"]
spreekwoord = spreekwoorden[random.randint(0, 3)]
spreekwoord_encrypted = ""
attempts_good = []
counter = 0

while counter < len(spreekwoord):
    if spreekwoord[counter] == " ":
        spreekwoord_encrypted += " "
        counter += 1
    else:
        spreekwoord_encrypted += "#"
        counter += 1

print("Dit spreekwoord moet je raden:", spreekwoord_encrypted)
attempt_first = True

while True:
    if attempt_first:
        keuze = input("Raad een letter of druk / als je denkt de uitdrukking te kennen: ")
        attempt_first = False
    else:
        keuze = input("Raad een letter: ")

    counter = 0

    if keuze != "/":
        while counter < len(spreekwoord):
            if spreekwoord[counter] == keuze:
                attempts_good.append(keuze)
            counter += 1
    else:
        if input("OK. Je denkt dat je het weet, zeg het maar: ") == spreekwoord:
            break

    counter = 0

    spreekwoord_builder = ""
    while counter < len(spreekwoord):
        if spreekwoord[counter] in attempts_good:
            spreekwoord_builder += spreekwoord[counter]
            counter += 1
        elif spreekwoord[counter] == " ":
            spreekwoord_builder += " "
            counter += 1
        else:
            spreekwoord_builder += "#"
            counter += 1

    if spreekwoord_builder == spreekwoord:
        break

    print("Dit resultaat heb je al:", spreekwoord_builder)

print("Ja, je hebt gewonnen!")



