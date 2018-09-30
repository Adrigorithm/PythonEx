leeftijd = int(input("Geef je leeftijd: "))

if leeftijd < 12:
    groep = "Welpen"
elif leeftijd < 15:
    groep = "Jongverkenners"
elif leeftijd < 18:
    groep = "Verkenners"
else:
    groep = "Jins"

print("Je wordt ingedeeld bij de " + groep)