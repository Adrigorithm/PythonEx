def C_to_K(celcius):
    return celcius * (9/5) + 32

celcius = float(input("Geef het aantal graden Celsius: "))
print(celcius, "graden Celsius =", C_to_K(celcius), "graden Fahrenheit")
