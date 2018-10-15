coordinate = input("Coordinate: ")
print("to")
coordinate2 = input("Coordinate: ")
possible = True
coordinate_calc = ""
counter = 1

while counter < 8:
    coordinate_calc = chr(ord(coordinate[0]) + counter) + str(int(coordinate[-1]) - counter)
    print(coordinate_calc)
    if coordinate_calc == coordinate2:
        print("possible")
        break
    counter += 1
