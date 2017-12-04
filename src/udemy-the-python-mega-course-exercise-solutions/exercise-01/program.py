def celsiusToFahrenheit(celsius):
    return celsius * 9 / 5 + 32

try:
    inputNumber = float(input("Celsius: "))
    print("Fahrenheit:", celsiusToFahrenheit(inputNumber))
except ValueError:
    print("Invalid number")
