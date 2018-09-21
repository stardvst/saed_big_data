import json

with open('cities.json', 'r') as f:
    data = json.load(f)
    for obj in data:
        for prop in obj["bars"]:
            if prop["chain"] == "Irish":
                print(obj["city"])

data = [{
    'fname': 'abcdef',
    'sname': 'ghijkl'
}, {
    'fname': 'abcdef',
    'sname': 'ghijkl'
}, {
    'fname': 'abcdef',
    'sname': 'ghijkl'
}, {
    'fname': 'abcdef',
    'sname': 'ghijkl'
}, {
    'fname': 'abcdef',
    'sname': 'ghijkl'
}, {
    'fname': 'abcdef',
    'sname': 'ghijkl'
}]

with open('a.json', 'w') as f:
    json.dump(data, f)


def fx(x):
    return x % 2


data = [1, 2, 3, 4, 5]
filtered_data = filter(fx, data)
print(*filtered_data)
