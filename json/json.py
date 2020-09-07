import json
print("json")
print("hi")
with open('example.json') as json_file:
    json_data = json.load(json_file)
print(json_data)