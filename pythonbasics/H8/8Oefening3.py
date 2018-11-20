"""
    LET OP:
        De resultaten in de opgaves blijken niet te kloppen.
"""

file = open("../H7/data/weerstation_2018 10.csv")
weerdata = []
datum_current = None
double_list = []
counter = 0
file_lenght = 0

while file.readline():
    file_lenght += 1

file.seek(0)

for row in file.readlines():
    if counter >= 1:
        row_split = row.split(";")
        if counter == 1:
            datum_current = row_split[0].split(" ")[0]

        if counter == file_lenght - 1 and len(double_list) > 0:
            weerdata.append([datum_current, sum(double_list) / len(double_list)])

        if row_split[0].split(" ")[0] != datum_current:
            weerdata.append([datum_current, sum(double_list) / len(double_list)])
            double_list = []
            datum_current = row_split[0].split(" ")[0]
        else:
            double_list.append(float(row_split[1]))
    counter += 1

print("Gemiddelde temperaturen:")

for weerdata_dag in weerdata:
    print(weerdata_dag[0] + "\t" + str(round(weerdata_dag[1], 2)))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
