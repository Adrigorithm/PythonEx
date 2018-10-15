numbers = [0, 45, 60, 13, 0, 42, 18, 17, 0, 26, 13]

counter = 0
odd_greatest = 0
index_value_0 = 0

while counter < len(numbers):
    odd_greatest= 0
    if numbers[counter] == 0:
        index_value_0 = counter
        counter += 1
        if counter == len(numbers):
            break
        while numbers[counter] != 0:
            if numbers[counter] % 2 != 0:
                if numbers[counter] > odd_greatest:
                    odd_greatest = numbers[counter]
            counter += 1
            if counter == len(numbers):
                break
        numbers[index_value_0] = odd_greatest
    else:
        counter += 1

print(numbers)

