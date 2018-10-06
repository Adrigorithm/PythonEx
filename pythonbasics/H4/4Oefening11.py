word = input("Geef een string: ")
counter = 0
word_new = ""

while counter < len(word):
    if counter == len(word) - 1:
        if word[counter] == "*":
            counter += 1
        else:
            word_new += word[counter]
            counter += 1
    elif word[counter] == "*" or word[counter - 1] == "*" or word[counter + 1] == "*":
        counter += 1
    else:
        word_new += word[counter]
        counter += 1

print(word_new)