import requests
import json

couchdb_url = 'https://couchdb-0036f3.smileupps.com/'

# data = {"00000": "11111"}
# # res = requests.post(couchdb_url + '/test', json=data)

# res = requests.get(couchdb_url + 'b36a4782225e761f6bb1b7f08d001ac8')
# entry = res.json()
# entry['aaa'] = 'bbb'
# requests.put(couchdb_url + entry["_id"], json=entry)

# with open('random.json') as f:
#    data = json.load(f)

db_name = "random_data_2"

res = requests.get(couchdb_url, auth=('admin', 'c84156afbc5e'))
print(res.status_code)

# create new database
res = requests.put(couchdb_url + db_name, auth=('admin', 'c84156afbc5e'))
# if res.status_code == 200:
#     print("Database {0} created.".format(db_name))

# print(len(data))
# for record in data:
#     requests.post(couchdb_url + db_name, json=record)
