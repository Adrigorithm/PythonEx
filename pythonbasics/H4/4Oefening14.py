word = input("Geef de te versleutelen tekst: ")
var_encryption = -1

while True:
    var_encryption = input("Geef het aantal karakters waarmee je wilt roteren: ")
    if var_encryption.isdigit():
        var_encryption = int(var_encryption)
        if var_encryption > 0:
            break

counter = 0
word_encrypted = ""

while counter < len(word):
    if word[counter].isupper():
        counter_encrypt = 0
        char_value = ord(word[counter])
        while counter_encrypt < var_encryption:
            if char_value == 90:
                char_value = 65
                counter_encrypt += 1
            else:
                char_value += 1
                counter_encrypt += 1
        word_encrypted += chr(char_value)

    elif word[counter].islower():
        counter_encrypt = 0
        char_value = ord(word[counter])
        while counter_encrypt < var_encryption:
            if char_value == 122:
                char_value = 97
                counter_encrypt += 1
            else:
                char_value += 1
                counter_encrypt += 1
        word_encrypted += chr(char_value)

    else:
        counter_encrypt = 0
        char_value = ord(word[counter])
        while counter_encrypt < var_encryption:
            if char_value == 255:
                char_value = 0
                counter_encrypt += 1
            else:
                char_value += 1
                counter_encrypt += 1
        word_encrypted += chr(char_value)

    counter += 1

print(word_encrypted)