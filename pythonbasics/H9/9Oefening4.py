import xml.etree.cElementTree as ET

file = ET.parse("startbestanden/medicijnen.xml")
root = file.getroot()

for bijsluiter in root:
    bijsluiter.find("benaming").text = bijsluiter.find("benaming").text.upper()
    bijsluiter.remove(bijsluiter.find("vormen"))

file.write("aangepast.xml")