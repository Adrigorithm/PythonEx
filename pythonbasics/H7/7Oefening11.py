from os.path import exists

if not exists("data/7Oefening10.txt"):
    file_new = open("data/7Oefening10.txt", "w")
    file_copy = open("7Oefening10.py")
    counter = 1
    counter_str = ""
    for record in file_copy.readlines():
        if counter < 10:
            counter_str = "   " + str(counter)
        elif counter < 100:
            counter_str = "  " + str(counter)
        elif counter > 1000:
            counter_str = " " + str(counter)
        else:
            counter_str = str(counter)
        file_new.write(counter_str + " " + record)
        counter += 1