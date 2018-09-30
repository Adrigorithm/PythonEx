ja = int(input("Aantal ja-stemmen: "))
neen = int(input("Aantal neen-stemmen: "))
blance = int(input("Aantal blanco-stemmen: "))
totaal = ja + neen + blance

print("Ja:", ja / totaal * 100)
print("Nee:", neen / totaal * 100)
print("Blanco", blance / totaal * 100)
