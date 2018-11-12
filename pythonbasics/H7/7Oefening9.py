file = open("data/weerstation_2018 08.csv")
temp_max = -10000

counter = 0
for record in file.readlines():
    if counter != 0:
        record = record[:-1]
        record_split = record.split(";")
        if float(record_split[1]) > temp_max:
            temp_max = float(record_split[1])
    counter += 1
print("De hoogste temperatuur in deze periode =", temp_max, "°C")