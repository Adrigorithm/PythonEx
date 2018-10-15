numbers = [2, 4, 5, 9]
list_0 = []

for int in numbers:
    list_0.append(0)
    list_0.append(0)

list_0[-1] = numbers[-1]

print(numbers)
print(list_0)