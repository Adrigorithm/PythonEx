word = input("Geef een string: ")
seq_greatest = 0
counter = 0
seq = 1

while counter + 1 < len(word):
    if word[counter] == word[counter + 1]:
        seq += 1
    else:
        seq = 1
    if seq > seq_greatest:
        seq_greatest = seq

    counter += 1
print("De lengte van het grootste blok in deze string is", seq_greatest)