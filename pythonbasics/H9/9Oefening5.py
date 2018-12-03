import xml.etree.cElementTree as ET

file = open("startbestanden/songs.txt", encoding="utf-8")

root = ET.Element("compilatie")

for row in file.readlines():
    row = row[:-1]
    row_split = row.split(";")
    track = ET.SubElement(root, "track")
    artist = ET.SubElement(track, "artist").text = row_split[0]
    song = ET.SubElement(track, "song").text = row_split[1]

xml_file = ET.ElementTree(root)
xml_file.write("songs.xml", encoding="utf-8", xml_declaration=True)
