dieren = ["kat", "hond", "muis", "rat", "eekhoorn", "uil", "mol"]
print("Orginele lijst:\t", dieren)

dieren_moved = []
counter = 0
string_last = ""

while counter < len(dieren):
    if counter == 0:
        string_last = dieren[counter]
        counter += 1
    else:
        dieren_moved.append(dieren[counter])
        counter += 1

dieren_moved.append(string_last)
print("Na het doorschuiven:\t", dieren_moved)