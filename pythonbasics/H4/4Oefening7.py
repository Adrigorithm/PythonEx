word = input("Geef een string met 'aan' (of niet): ")
index = word.find("aan")

if index > 1:
    print("'aan' komt wel voor maar niet vooraan in de string")

elif index > -1:
    print("'aan' komt voor op de eerste of tweede plaats")

else:
    print("'aan' komt niet voor")