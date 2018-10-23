#    r0755939
#    Adriaan Waem
#    1 ITF E
#    Reeks 2

string = input("Voer je voornaam en naam in: ")

print("Welkom", string)
for counter in range (0, len(string) - 1):
    print("-", end="")

print("--------")

for counter in range (0, len(string)):
    print(string[:counter + 1])