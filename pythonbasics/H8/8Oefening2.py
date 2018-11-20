file = open("../H7/data/vakinfostudenten.csv", encoding="utf-8")
file_new = open("../H7/data/studentenvakken.txt", "w")
info = []
counter = 0
counter_dupe = 0

for row in file.readlines():
    row = row[:-1]
    row_split = row.split(";")
    if counter >= 1:
        info.append(row_split[3] + ";")
        info.append(row_split[4] + ";")
        info.append(row_split[5] + ";")
        info.append(row_split[1] + "(" + row_split[2] + ")")
    counter += 1

counter = 0

while counter < len(info):
    if counter >= 4 and counter % 4 == 0:
        if info[counter] == info[counter - 4]:
            file_new.write(";")
            counter += 3
        else:
            file_new.write("\n")
            file_new.write(info[counter])
            counter += 1
    else:
        file_new.write(info[counter])
        counter += 1

file.close()
file_new.close()
