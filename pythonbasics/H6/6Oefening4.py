import random

def list_random(amount, min, max):
    random_list = []

    for count in range(0, amount):
        random_list.append(random.randint(min,max))

    return random_list

def list_primkey(list):
    return set(list)

amount = int(input("Met hoeveel dobbelstenen wil je gooien? "))
poker = input("Poker? (y/n): ")

if poker == "y":
    attempts = 1
    while True:
        worp = list_random(amount, 1, 6)
        print(worp)
        if len(list_primkey(worp)) == 1:
            print("Je gooide poker na", attempts, "keer")
            break
        attempts += 1
else:
    worp = list_random(amount, 1, 6)
    print("Je gooide:", worp)
    print("Je unieke worpen waren:", list_primkey(worp))
