import random

maximum = int(input("Geef het maximale getal voor hoger/lager (0 - ?): "))
ans = random.randint(0, maximum + 1)

# Hier kun je ook een statisch getal opvragen dmv input

getal = ''
error = 0
while getal != ans:
    getal = int(input("Geef een positief getal: "))
    if getal < ans:
        print("Hoger!")
        error += 1
    elif getal > ans:
        print("Lager!")
        error += 1
error += 1
print("Je hebt het getal", ans, "geraden in", error, "beurten")


