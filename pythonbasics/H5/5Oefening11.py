python_klassen = [["1ITFA", 42]]
klassen = ("A", "B", "C", "D", "E", "F", "G", "H")
counter = 1

while counter < len(klassen):
    students = int(input("Hoeveel studenten zitten in 1ITF" + klassen[counter] + ": "))
    klas = ["1ITF" + klassen[counter], students]
    python_klassen.append(klas)
    counter += 1

for list in python_klassen:
    print(list)