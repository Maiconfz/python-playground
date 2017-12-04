def celsiusToFahrenheit(celsius):
    return celsius * 9 / 5 + 32

temperatures = [10,-20, -289, 100]

for inputNumber in temperatures:
    if inputNumber < -273.15:
        print("That temperature doesn't make sense!")
    else:
        print("Fahrenheit:", celsiusToFahrenheit(inputNumber))
