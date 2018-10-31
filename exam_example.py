import json


def have_common_chain(city1, city2):
    with open('cities.json') as f:
        data = json.load(f)

    company1 = None
    company2 = None

    for company in data:
        if company["city"] == city1:
            company1 = company
        elif company["city"] == city2:
            company2 = company
        if company1 and company2:
            break

    comp1_bars = set(map(lambda bar: bar["chain"], company1["bars"]))
    comp2_bars = set(map(lambda bar: bar["chain"], company2["bars"]))

    return len(comp1_bars & comp2_bars) > 0


with open('cities.json') as f:
    data = json.load(f)

# cities with most bars
cities = map(lambda company: company["city"],
             filter(lambda company: len(company["bars"]) == max(
                    map(lambda x: len(x),
                        map(lambda company: company["bars"], data))), data))

print(*cities)

# does pair of cities have common chain?


print(have_common_chain('CARLOS', 'GUILFORD'))
