from functools import reduce
import json
import requests

url = "https://api.twitter.com/oauth/authenticate"
res = requests.get(url)
headers = {
    "authorization": "OAuth oauth_consumer_key=\"DmYWN7UCWou50kIyolmZzbcE6\", \
    oauth_signature_method=\"HMAC-SHA1\", \
    oauth_token=\"2985848154-VCvU8SxzsuTGWl4sZBrioqYqPMK81ed7kC07lRV\", \
    oauth_version =\"1.0\""
}
res = requests.get(url, headers=headers)
print(res.text)

with open('people.json') as f:
    people = json.load(f)

max_friend_count = max(map(lambda person: len(person["friends"]), people))
max_friends = map(lambda person: person["name"],
                  filter(lambda person: len(person["friends"]) ==
                         max_friend_count,
                         people))

print(list(max_friends))

blue_eyes_friend_count = max(map(lambda person: len(list(
    filter(lambda friend: friend["eyeColor"] == "blue", person["friends"]))),
    people))

max_blue_eyes_friends = map(
    lambda person: person["name"],
    filter(
        lambda person: len(list(
            filter(lambda friend: friend["eyeColor"] == "blue",
                   person["friends"]))) == blue_eyes_friend_count,
        people))

print(list(max_blue_eyes_friends))

# 2
l = list(filter(lambda x: x > 2, range(-100, 100, 2)))
print(l)

# 3
print(reduce(lambda x, y: x + y, map(lambda x: x**4, range(1, 100))))

# 4


def caller(f, g, a):
    return f(g(a))


def plus_1(x):
    return x, x + 1


print(caller(max, plus_1, 10))
