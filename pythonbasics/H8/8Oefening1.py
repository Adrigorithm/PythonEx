file = open("../H7/data/examenlokalen.txt", encoding="utf-8")
counter = 0
counter_row = 0
lokaal = ""

for row in file.readlines():
    row = row[:-1]
    row_split = row.split(";")
    if counter == 0:
        lokaal = row_split[2]
        counter += 1
        print(lokaal)
    if lokaal != row_split[2]:
        print("Aantal studenten in lokaal " + lokaal + " =", counter_row)
        print()
        print(row_split[2])
        lokaal = row_split[2]
        print("\t" + row_split[1] + " " + row_split[0])
        counter_row = 1
    else:
        print("\t" + row_split[1] + " " + row_split[0])
        counter_row += 1
    counter += 1

print("Aantal studenten in lokaal " + lokaal + " =", counter_row)
