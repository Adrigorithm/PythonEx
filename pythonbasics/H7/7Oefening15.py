file1 = open("data/voorraad1.txt")
file2 = open("data/voorraad2.txt")
file_new = open("data/voorraad_samen.txt", "w")
counter = 1
blacklist = []

file_new.write("artikelnummer;voorraad\n")

for record in file1.readlines():
    if counter > 1:
        record_split = record.split(";")
        artikel = record_split[0]
        counter1 = 1

        file2.seek(0)
        for record1 in file2:
            if counter1 > 1:
                record_split1 = record1.split(";")
                artikel1 = record_split1[0]
                if artikel == artikel1:
                    blacklist.append(artikel)
                    file_new.write(artikel + ";" + str(int(record_split[1]) + int(record_split1[1])) + "\n")
            counter1 += 1
    counter += 1

file1.seek(0)
file2.seek(0)

counter = 1
for record in file1.readlines():
    if counter > 1:
        record_split3 = record.split(";")
        if record_split3[0] not in blacklist:
            file_new.write(record)
    counter += 1

counter = 1
for record in file2.readlines():
    if counter > 1:
        record_split4 = record.split(";")
        if record_split4[0] not in blacklist:
            file_new.write(record)
    counter += 1