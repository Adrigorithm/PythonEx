word = input("Geef een woord: ")
counter = 0

while counter < len(word):
    if counter == len(word) - 1:
        print (word[counter])
    elif counter == len(word) - 2:
        print (word[counter] + word[counter + 1])
    else:
        print(word[counter + 1] + word[counter + 2] + word[counter], end="")
    counter += 3