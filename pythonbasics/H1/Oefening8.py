huidige_uur = int(input("Geef het huidige uur: "))
wachten = int(input("Hoe lang wil je wachten: "))
count = 0

while count < wachten:
    huidige_uur += 1
    if huidige_uur > 24:
        huidige_uur = 1
    count += 1
print("Het alarm zal afgaan om " + str(huidige_uur) + "u")