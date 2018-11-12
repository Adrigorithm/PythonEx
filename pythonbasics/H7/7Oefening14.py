file = open("data/hamlet.txt")
file_new = open("data/hamlet2.txt", "w")
file_new_new = open("data/hamlet3.txt", "w")

klinkers = ("a", "i", "e", "o", "u", "y")
leestekens = (",", ".", "...")
file_new_count = 0

for record in file.readlines():
    del_spacing = False
    for char in record:
        if del_spacing:
            if char != " ":
                del_spacing = False
                file_new.write(" " + char)
                file_new_count += 1
        else:
            if char in leestekens:
                del_spacing = True
            file_new.write(char)
            file_new_count += 1
file.close()
file_new.close()
file_new = open("data/hamlet2.txt")
file_new_new_count = 0

for record in file_new.readlines():
    for char in record:
        if char.lower() not in klinkers:
            file_new_new.write(char)
            file_new_new_count += 1

print("De invoerfile bevat:", file_new_count, "karakters")
print("De uitvoerfile bevat:", file_new_new_count, "karakters")
