import json


def microsoft_checks(data):
    total = 0
    for obj in data:
        for props in obj["company"]:
            if props["name"] == "Microsoft":
                total += obj["bars"][0]["check"]
    return total


def amazon_coffee(data):
    count = 0
    for obj in data:
        for props in obj["company"]:
            if props["name"] == "Amazon" and props["industry"] == "Coffee":
                count += 1
    return count


def cities_without_a(data):
    cities = set()
    for obj in data:
        if 'a' not in str(obj["city"]).lower():
            cities.add(str(obj["city"]).capitalize())
    return list(cities)


def facebook_industries(data):
    industries = set()
    for obj in data:
        for props in obj["company"]:
            if props["name"] == "Facebook":
                industries.add(props["industry"])
    return list(industries)


with open('cities.json') as f:
    data = json.load(f)

    print('Data length:', len(data), end='\n\n')

    print('Microsoft checks total:', microsoft_checks(data), end='\n\n')
    print('Amazon coffee count:', amazon_coffee(data), end='\n\n')
    print('Cities without \'a\':', cities_without_a(data), end='\n\n')
    print('Facebook industries:', facebook_industries(data))
