import random
if random.randint(0,2) == 0:
    keuze_pc = "blad"
elif random.randint(0,2) == 1:
    keuze_pc = "steen"
else:
    keuze_pc = "schaar"

# Je kunt ook een 'domme' AI gebruiken door een statische waarde in te geven.
# vervang code hierboven door:
# keuze_pc = "blad" of keuze_pc = "steen" of keuze_pc = "schaar"

keuze = input("Wat kies jij: blad, steen of schaar? ")
print("Jij koos " + keuze)
print("Ik koos " + keuze_pc)

if keuze == "blad" and keuze_pc == "steen" or keuze == "steen" and keuze_pc == "schaar" or keuze == "schaar" and keuze_pc == "blad":
    print("Jij wint")
elif keuze == keuze_pc:
    print("Gelijkspel")
else:
    print("Ik win")