word = input("Encoded: ")
counter = 0
string_builder = ""

while counter < len(word):
    if word[counter] == " ":
        string_builder += " "
        counter += 1

    elif ord(word[counter]) < 97 or ord(word[counter]) > 122:
        string_builder += word[counter]
        counter += 1
    else:
        code = ord(word[counter])
        if code == 121:
            code  = 97
        elif code == 122:
            code = 98
        else:
            code += 2

        string_builder += chr(code)
        counter += 1

print(string_builder)

# url, test this app with 'map' -> 'ocr'