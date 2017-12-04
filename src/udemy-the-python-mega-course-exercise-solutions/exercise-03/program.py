def celsiusToFahrenheit(celsius):
    return celsius * 9 / 5 + 32

try:
    inputNumber = float(input("Celsius: "))

    if inputNumber < -273.15:
        print("Invalid celsius value")
    else:
        print("Fahrenheit:", celsiusToFahrenheit(inputNumber))
except ValueError:
    print("Invalid number")
