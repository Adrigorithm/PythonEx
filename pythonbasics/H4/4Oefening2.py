word = input("Geef een (oneven aantal chars) string: ")
word_lenght = len(word)
print(word[round(word_lenght / 2) - 2:round(word_lenght / 2) + 1])
