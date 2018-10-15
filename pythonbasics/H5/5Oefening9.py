string = input("Geef een tekst: ")
string_list = []
counter = 0

while counter < len(string):
    if string[counter] != " ":
        if string[counter] not in string_list:
            string_list.append(string[counter])
    counter += 1

string_list.sort()

for str in string_list:
    print(str, end=" ")