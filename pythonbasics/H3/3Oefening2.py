getal = input("Geef een getal: ")
count = 1
amount_6 = 0
amount_0 = 0

while (count <= len(getal)):
    if getal[count-1:count] == "6":
        amount_6 += 1
    elif getal[count-1:count] == "0":
        amount_0 += 1
    count += 1

print("Het getal bestaat uit", amount_0, "nullen en", amount_6, "zessen")
