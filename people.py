import json

with open('generated.json') as f:
    data = json.load(f)

cities = map(lambda person: person["address"].split(', ')[1], data)

people = map(lambda city:
             list(map(lambda person: (person["name"], city),
                      filter(lambda person:
                             person["address"].split(', ')[1] == city, data))),
             cities)

print(*people)
