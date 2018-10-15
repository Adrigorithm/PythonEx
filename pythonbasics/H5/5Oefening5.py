numbers = (8, 5, 3, 7, 5, 6, 7, 3, 8, 2)
print(numbers)

counter = 0
last_4 = -1

while counter < len(numbers):
    if numbers[counter] == 4:
        last_4 = counter
    counter += 1

if last_4 == -1:
    print("Het getal 4 komt niet voor in de List")
else:
    numbers_ex4 = numbers[last_4 + 1:]
    print(numbers_ex4)