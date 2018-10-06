word = input("Geef een string: ")
tripels = 0
counter = 0

while counter <= len(word) - 2:
    if word[counter] == word[counter + 1] and word[counter] == word[counter + 2]:
        tripels += 1;
    counter += 1

if tripels == 0:
    print("Er zijn geen triples in deze string")
elif tripels == 1:
    print("Er is 1 triple in deze string")
else:
    print("Er zijn", tripels, "tripels in deze string")