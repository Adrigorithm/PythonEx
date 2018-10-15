print("Geef je naam en de afstand naar school.\nTyp stop als naam wanneer je de invoer wenst af te sluiten.")

name = []
distance = []

while True:
    name_current = input("Je naam: ")
    if name_current == "stop":
        break
    else:
        name.append(name_current)
        distance.append(float(input("Afstand naar school: ")))

if len(name) > 0:
    print("Overzicht")

    counter = 0

    while counter < len(name):
        print(str(distance[counter])+"\t"+name[counter])
        counter += 1

    max_distance = distance.index(max(distance))

    print(name[max_distance], "woont het verst, namelijk", distance[max_distance], "km")
    print("De gemiddelde afstand is", sum(distance) / len(distance))
