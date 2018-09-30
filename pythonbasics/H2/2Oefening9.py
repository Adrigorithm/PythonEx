kg = int(input("Geef je gewicht in kilogram: "))
lenght = int(input("Geef je lengte in centimeter: "))
bmi = kg / lenght**2 * 10000

print("Een persoon van", kg, "kg met een lengte van", lenght, "cm heeft als BMI", bmi)
if bmi < 18:
    print("ondergewicht")
elif bmi < 25:
    print("normaal gewicht")
elif bmi < 27:
    print("light overgewicht")
elif bmi < 30:
    print("matig overgewicht")
elif bmi < 40:
    print("ernstig overgewicht")
else:
    print("ziekelijk overgewicht")