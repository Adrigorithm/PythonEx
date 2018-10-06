word = input("Geef een string: ")
brood1_index = word.find("brood")
word_sub = word[brood1_index + 5:]
brood2_index = word_sub.find("brood")
word = word_sub[:brood2_index]

print(word)