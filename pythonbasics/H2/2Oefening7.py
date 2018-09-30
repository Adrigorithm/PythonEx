wijn = int(input("Hoeveel flessen wijn zijn er: "))
pizza = int(input("Hoeveel pizza's zijn er: "))
if wijn > 4 and pizza > 4:
    if wijn == pizza * 2 or pizza == wijn * 2:
        print("Dit is een fantastisch feestje")
    else:
        print("Dit is een goed feestje")
else:
    print("Dit is maar een stom feestje")