begingrens = int(input("Geef de begingrens: "))
eindgrens = int(input("Geef de eindgrens: "))
tussen_uitkomsten = begingrens

if begingrens > eindgrens:
    print("De begingrens moet kleiner zijn dan de eindgrens!")
elif begingrens == eindgrens:
    print("Som van getallen van", begingrens, "t.e.m.", eindgrens)
    print(begingrens)
else:
    print("Som van getallen van", begingrens, "t.e.m.", eindgrens)
    while begingrens < eindgrens:
        tussen_uitkomsten += begingrens + 1
        print("+", begingrens + 1, "-->", tussen_uitkomsten)
        begingrens += 1
