leeftijd_zoon = int(input("Hoe oud ben jij: "))
leeftijd_vader = int(input("Hoe oud is je vader: "))

if leeftijd_vader < leeftijd_zoon * 2:
    print("De situatie is voor jullie leeftijden niet meer mogelijk")
else:
    while leeftijd_vader != 2 * leeftijd_zoon:
        leeftijd_zoon += 1
        leeftijd_vader += 1

    print("Je vader is dan", leeftijd_vader, "en jij", leeftijd_zoon)