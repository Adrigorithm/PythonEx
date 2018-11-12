from random import randint

int_random = randint(1, 10)
counter = 1

file = open("data/tafels van " + str(int_random) + ".txt", "w")

while counter < 11:
    file.write(str(counter) + "x" + str(int_random) + "=" + str(counter * int_random) + "\n")
    counter += 1