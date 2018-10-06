counter = 0
words = []

while counter < 5:
    words.append(input("Geef woord " + str(counter + 1) + ": ").capitalize())
    counter += 1

counter = 4

while counter > -1:
    print(words[counter], end=" ")
    counter -= 1