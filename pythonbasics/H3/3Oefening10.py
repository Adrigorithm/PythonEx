treden = int(input("Hoeveel treden heeft de trap: "))
count = 1

while count <= treden:
    output = "#####" * count
    print(output + "\n" + output)
    count += 1