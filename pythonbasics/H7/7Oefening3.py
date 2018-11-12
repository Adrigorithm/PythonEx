file = open("data/voornamen.txt")
file_format = file.readlines()

counter = 1
for string in file_format:
    string = string[:-1]
    if counter % 10 == 0:
        print(string, end="\n")
    else:
        print(string, end="\t")
    counter += 1
file.close()
