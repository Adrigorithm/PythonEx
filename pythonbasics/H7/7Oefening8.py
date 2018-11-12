file = open("data/contactpersonen.csv")

meisjes = []
jongens = []

for record in file.readlines():
    record = record[:-1]
    record_split = record.split(";")

    if record_split[3] == "V":
        meisjes.append(record_split[1] + " " + record_split[0])
    else:
        jongens.append(record_split[1] + " " + record_split[0])

print(len(meisjes), "meisjes:")
for name in sorted(meisjes):
    print("\t"+ name)

print(len(jongens), "jongens:")
for name in sorted(jongens):
    print("\t" + name)