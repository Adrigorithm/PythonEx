import xml.etree.cElementTree as ET

file = ET.parse("startbestanden/plant_catalog.xml")
root = file.getroot()
counter = 1
for plant in root.iter("plant"):
    if (plant.find("light").text == "SUN"):
        print("Plant " + str(counter) + " : " + plant.find("common").text + " (" + plant.find(
            "botanical").text.capitalize() + ")")
        counter += 1