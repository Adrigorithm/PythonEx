file = open("data/playlist.txt", encoding="utf-8")

print("Playlist")

for record in reversed(file.readlines()):
    record = record[:-1]
    record_split = record.split(";")
    print(record_split[0] + "\t" + record_split[1] + " (" + record_split[2].lower() + ")")