file = open("data/in de stille kempen.txt")
string = ""

for record in file.readlines():
    if len(record) > len(string):
        string = record

print("De langste regel in deze tekst heeft", len(string), "karakters")
print(string)