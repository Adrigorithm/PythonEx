fibonacchi = []
limit = int(input("Tot hoever wil je de reeks van Fibonacci drukken? "))
counter = 0

while True:
    if counter == 0:
        fibonacchi.append(0)
    elif counter == 1 or counter == 2:
        fibonacchi.append(1)
    else:
        fibonacchi.append(fibonacchi[counter - 1] + fibonacchi[counter - 2])

    if fibonacchi[counter] <= limit:
        print(fibonacchi[counter], end=" ")
    else:
        break
    counter += 1
