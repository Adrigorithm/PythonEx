getal_next = 0
getal_next = int(input("Geef een getal, stop door een negatief getal in te geven: "))
numbers = []

# numbers = [] is een variabele van het type List. Hiermee kun je meerdere variabelen van eenzelfde type opslaan, perfect voor deze oefening.
# een andere optie is bijvoorbeeld de String.join property.
# google is je vriend.

while getal_next >= 0:
    getal = int(input("Geef een positief getal: "))
    numbers.append(getal)
    getal_next = int(input("Geef een getal, stop door een negatief getal in te geven: "))

print("De som van de", len(numbers), "getallen is", sum(numbers))
