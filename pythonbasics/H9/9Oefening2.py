import xml.etree.cElementTree as ET

file = ET.parse("startbestanden/bioscoopoverzicht.xml")
root = file.getroot()

print("Bioscopen in Antwerpen")

for bioscoop in root:
    if bioscoop.find("district").text == "Antwerpen":
        print(bioscoop.find("naam").text + "\n" + bioscoop.find("straat").text + " " + bioscoop.find("huisnummer").text + "\n" + bioscoop.find("postcode").text + " " + bioscoop.find("district").text + "\n")