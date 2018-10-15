numbers = [23, 12, 54, 85, 46, 30, 26, 64, 91]
print(numbers, "wordt nu")

numbers_even =[]
numbers_odd = []
numbers_sorted = []

for int in numbers:
    if int % 2 == 0:
        numbers_even.append(int)
    else:
        numbers_odd.append(int)

numbers_sorted.extend(numbers_even + numbers_odd)
print(numbers_sorted)