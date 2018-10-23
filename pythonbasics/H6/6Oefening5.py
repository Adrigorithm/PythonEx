def count_capitals(string):
    capitals = 0
    lower = 0
    for counter in range (0, len(string)):
        if string[counter].islower():
            lower += 1
        if string[counter].isupper():
            capitals += 1
    results = (capitals, lower)
    return results

pwd = input("Password? (y/n): ")

if pwd == "y":
    while True:
        pwd = input("Stel je wachtwoord in. (min 2 hoofdletters en min 3 kleine letters): ")
        if count_capitals(pwd)[0] >= 3 and count_capitals(pwd)[1] >= 4:
            break
else:
    string = input("Te testen string: ")

    print(count_capitals(string)[0])
    print(count_capitals(string)[1])