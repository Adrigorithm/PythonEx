"""
    LET OP:
        De resultaten in de opgaves blijken niet te kloppen.
"""

file = open("../H7/data/sponsors.txt", encoding="utf-8")
sponsor_data = []

for row in file.readlines():
    row = row[:-1]
    row_split = row.split("*")
    sponsor_data.append([row_split[0], row_split[1] + " " + row_split[2], row_split[3]])

print("Overzicht giften")
print("Nummer\tSponsor\t\t\tBedrag")

counter_attest = 0

for data in sponsor_data:
    if float(data[2]) >= 40:
        print(data[0] + "\t" + data[1] + "\t" + str(data[2]) + " **")
        counter_attest += 1
    else:
        print(data[0] + "\t" + data[1] + "\t" + str(data[2]))

print("Er moeten", counter_attest, "fiscale attesten verstuurd worden.")
