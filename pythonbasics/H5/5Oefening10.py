string = input("Geef je string van karakters door: ")
counter = 0
string_number = []
string_alpha = []

while counter < len(string):
    if string[counter].isdigit():
        string_number.append(string[counter])
        counter += 1
    elif string[counter].isalpha():
        string_alpha.append(string[counter])
        counter += 1
    else:
        counter += 1

string_alpha.sort()
string_alpha.reverse()
string_number.extend(string_alpha)
print(string_number)