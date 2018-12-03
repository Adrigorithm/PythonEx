import xml.etree.cElementTree as ET

file = ET.parse("startbestanden/jobkrant.xml")
counter = 1

for bedrijf in file.iter("bedrijf"):
    for vacature in bedrijf.find("vacatures"):

        attribute = vacature.find("functie").attrib
        
        if attribute["groep"] == "IT":
            print(str(counter) + "." + "\tFunctie:\t" + vacature.find("functie").text)
            print("\tBedrijf:\t" + bedrijf.find("naam").text)
            print("\tContact:\t" + bedrijf.find("contactpersoon").find("email").text)
            counter += 1
            print()