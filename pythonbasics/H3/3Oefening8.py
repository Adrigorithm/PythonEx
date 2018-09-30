eindcijfer = input("Op welk eindcijfer wil je de getallen controleren: ")
count = 0
error = 0

while count < 10:
    getal = int(input("Geef een getal: "))
    if str(getal)[-1:] == eindcijfer:
        error += 1
    count += 1

print(error, "van de 10 getallen eindigen op " + eindcijfer)