from os.path import exists


def weergegevens_maand(maand):
    gegevens = ["", -10000.0, "", ""]
    # [periode, temp_hoogst, temp_hoogst_time, temp_hoogst_date]

    if exists("data/weerstation_2018 " + maand + ".csv"):
        file = open("data/weerstation_2018 " + maand + ".csv")
        counter = 1
        record_split = []

        for record in file.readlines():
            if counter > 1:
                record = record[:-1]
                record_split = record.split(";")
                if counter == 2:
                    gegevens[0] += record_split[0]
                if float(record_split[1]) > float(gegevens[1]):
                    gegevens[1] = record_split[1]
                    record_split_split = record_split[0].split(" ")
                    gegevens[2] = record_split_split[1]
                    gegevens[3] = record_split_split[0]
            counter += 1

        gegevens[0] += " - " + record_split[0]
        return gegevens
    else:
        return None


maand = ""

while maand not in range(1, 13):
    maand = int(input("Van welke maand wil je de weergegevens zien: "))

maand = str(maand)

if maand == "8":
    maand = "08"

gegevens = weergegevens_maand(maand)

if gegevens is not None:
    print()
    print("Periode:", gegevens[0])
    print("-------")
    print("De hoogste temperatuur in deze periode =", gegevens[1], "°C")
    print("Deze temperatuur werd opgemeten om " + gegevens[2] + "u op", gegevens[3])
else:
    print("Over deze maand zijn geen gegevens beschikbaar!")
