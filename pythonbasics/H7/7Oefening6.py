import random

file_number = random.randint(1, 3)
file = open("data/wens" + str(file_number) + ".txt")

print("Afdruk van bestand", file_number)
print()
print(file.read())

