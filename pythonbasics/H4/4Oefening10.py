word = input("Geef een string: ")

x_last_index = -1
y_last_index = -1
counter = 0

while counter < len(word):
    if word[counter] == "x":
        x_last_index = counter
    if word[counter] == "y":
        y_last_index = counter
    counter += 1

if y_last_index > x_last_index:
    print("In de gegeven tekst zijn x en y in evenwicht.")
else:
    print("In de gegeven tekst zijn x en y NIET in evenwicht.")