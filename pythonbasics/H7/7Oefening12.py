from os.path import exists

if exists("data/7Oefening10.txt") and not exists("data/7Oefening10_noAI.txt"):
    file = open("data/7Oefening10.txt")
    file_new = open("data/7Oefening10_noAI.txt", "w")

    for record in file.readlines():
        file_new.write(record[5:])