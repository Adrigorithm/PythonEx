file = open("data/voornamen.txt")
record = file.readline()
records = 0
records_z = 0
while record:
    if record != "\n":
        if record.__contains__("Z") or record.__contains__("z"):
            print(record.rstrip())
            records_z += 1
        records += 1
        record = file.readline()

file.close()
print("Er zijn", records, "voornamen in het bestand.")
print(records_z, "daarvan bevatten een letter z.")