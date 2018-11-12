file = open("data/voornamen.txt")
file_list = file.readlines()
for record in reversed(file_list):
    if record.endswith("\n"):
        record = record[:-1]
        print(record)