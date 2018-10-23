def eur_usd_conversion(eur_to_usd, eur):
    return eur * eur_to_usd

eur_to_usd = float(input("Geef de huidige wisselkoers (€ -> $): "))
eur = float(input("Geef je bedrag in Euro: "))

print("€", eur, "= $", eur_usd_conversion(eur_to_usd, eur))
