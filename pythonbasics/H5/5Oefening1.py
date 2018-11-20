dieren = ["kat", "hond", "muis", "rat", "eekhoorn", "uil", "mol"]
print(dieren)

temp = dieren[0]
dieren[0] = dieren[-1]

# of in een regel: dieren[0], dieren[-1] = dieren[-1], dieren[0]

dieren[-1] = temp

print(dieren)