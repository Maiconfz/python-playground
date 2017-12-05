import json

file = open("data.json", 'r')
data = json.load(file)
file.close()
print(data)