import sys
import requests

if len(sys.argv) != 3:
    print("usage: <program> <search_key> <limit>")
    sys.exit()

api_key = "aQokno4KlaLflzQlg2aRAxvqhdaQs9hU"
endpoint = "https://api.giphy.com/v1/gifs/search?q={0}&api_key={1}&limit={2}" \
    .format(sys.argv[1], api_key, sys.argv[2])

res = requests.get(endpoint, auth=("mlilia", api_key))
data = res.json()

# print urls
for obj in data["data"]:
    print(obj["url"])
