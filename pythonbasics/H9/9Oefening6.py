import xml.etree.cElementTree as ET

def keuze_print(keuze_tuple):
    keuze = ''
    while keuze.upper() not in keuze_tuple:
        keuze = input("Wil je de plantenlijst\n\tA: alfabetisch\n\tD: volgens prijs (hoog naar laag)\n\tS: volgens prijs (laag naar hoog)\nJouw keuze: ").upper()
    return keuze

def prijslijst_print(prijslijst, keuze):
    output = []
    counter = 0
    if keuze == 'A':
        prijslijst.sort()
        return prijslijst
    elif keuze == 'D':
        while counter < len(prijslijst):
            counter_output = 0

            while counter_output < len(output) or counter_output == 0:
                if len(output) == 0:
                    output.append(prijslijst[counter])
                    break;
                elif float(output[counter_output][1][1:]) > float(prijslijst[counter][1][1:]):
                    output.insert(counter_output, prijslijst[counter])
                    break;
                elif counter_output == len(output) - 1:
                    output.append(prijslijst[counter])
                    break;
                else:
                    counter_output += 1
            counter += 1
        output.reverse()
        return output
    else:
        while counter < len(prijslijst):
            counter_output = 0

            while counter_output < len(output) or counter_output == 0:
                if len(output) == 0:
                    output.append(prijslijst[counter])
                    break;
                elif float(output[counter_output][1][1:]) > float(prijslijst[counter][1][1:]):
                    output.insert(counter_output, prijslijst[counter])
                    break;
                elif counter_output == len(output) - 1:
                    output.append(prijslijst[counter])
                    break;
                else:
                    counter_output += 1
            counter += 1
        return output

file = ET.parse("startbestanden/plant_catalog.xml")
root = file.getroot()
prijslijst = []

for plant in root:
    prijslijst.append([plant.find("common").text, plant.find("price").text])

keuze_tuple = ('A', 'D', 'S')
keuze = keuze_print(keuze_tuple)

output = prijslijst_print(prijslijst, keuze)

for lijst in output:
    print(lijst[1] + " | " + lijst[0])


