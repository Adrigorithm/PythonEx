word = input("Mess: ")
counter_ord = 32
char = []
rarity = []

while counter_ord < 127:
    counter = 0
    char_rarity = 0
    while counter < len(word):
        if word[counter] == chr(counter_ord):
            char_rarity += 1
        counter += 1
    char.append(chr(counter_ord))
    rarity.append(char_rarity)
    counter_ord += 1

print()

#tested characters

print(char)

#amount of above characters in the string

print(rarity)
print()

counter = 0

while counter < len(rarity):
    if rarity[counter] == 1:
        print(char[counter], end="")
    counter += 1

# unscrambled = 'equality'