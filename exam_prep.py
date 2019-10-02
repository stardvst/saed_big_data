import json
import requests

url = 'https://couchdb-77e6b0.smileupps.com/'
# res = requests.get(url,
#                    auth=('admin', 'b4c248c17562'))
# entry = res.json()
# entry['a'] = 'r'

# url = 'https://couchdb-77e6b0.smileupps.com/test/' + entry["_id"]
# res = requests.put(url, json=entry)
# print(res.text)

with open('random.json') as f:
    data = json.load(f)

db_name = "random_data_2"

res = requests.get(url, auth=('admin', 'b4c248c17562'))
print(res.status_code)

# create new database
res = requests.put(url + db_name, auth=('admin', 'b4c248c17562'))
if res.status_code == 200:
    print("Database {0} created.".format(db_name))

print(len(data))
for record in data:
    requests.post(url + db_name, json=record)
