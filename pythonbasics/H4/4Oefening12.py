while True:
    naam  = input("Voer een naam in (enter om te stoppen): ")
    keuze = ""
    if naam == "":
        exit()
    else:
        print()
        print("Keuzemenu:")
        print("**********")
        print("H Hoofdletters")
        print("K Kleine letters")
        print("A AfGeWiSsElD")
        print("**********")


        while keuze not in {"H", "K", "A"}:
            keuze = input("Maak je keuze (H-K-A)").capitalize()

        if keuze == "H":
            print(naam.upper())
        elif keuze == "K":
            print(naam.lower())
        else:
            counter = 0
            while counter < len(naam):
                if counter % 2 == 1:
                    print(naam[counter].lower(), end="")
                    counter += 1
                else:
                    print(naam[counter].upper(), end="")
                    counter += 1
            print()
        print()
