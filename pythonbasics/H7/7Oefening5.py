file = open("data/boeken.txt")

counter = 1
counter_output = 1
for record in file.readlines():
    record = record[:-1]
    if counter % 2 == 1:
        print(str(counter_output) + ". " + record + " -> ", end="")
        counter_output += 1
    else:
        print(record)
    counter += 1
file.close()