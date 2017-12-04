def celsiusToFahrenheit(celsius):
    return celsius * 9 / 5 + 32

def saveToFile(text, fileName):
    file = open(fileName, "a")
    file.write(str(text) + "\n")
    file.close();
    

temperatures = [10,-20, -289, 100]

for inputNumber in temperatures:
    if inputNumber < -273.15:
        print("That temperature doesn't make sense!")
    else:
        fah = celsiusToFahrenheit(inputNumber)
        print("Fahrenheit:", fah)
        saveToFile(fah, "output.txt")
