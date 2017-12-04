import glob2
from datetime import datetime


fileNames = glob2.glob("*.txt")
now = datetime.now()
outputFileFileName = now.strftime("%Y-%m-%d-%H-%M-%S-%f.txt")

with open(outputFileFileName, "w") as outputFile:
    for fileName in fileNames:
        with open(fileName) as inputFile:
            outputFile.write(inputFile.read() + "\n")
