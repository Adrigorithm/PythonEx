word = input("Geef een woord: ")
counter = len(word) - 1
word_reverse = ""

while counter >= 0:
    word_reverse += word[counter]
    counter -= 1

if word.lower() != word_reverse.lower():
    print(word, "is geen palindroom")
else:
    print(word, "is een palindroom")