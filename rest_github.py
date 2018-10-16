import requests
from requests.auth import HTTPBasicAuth

# url = "http://ipinfo.io/8.8.8.8/"

# res = requests.get(url)
# if res.status_code == 200:
#     data = res.json()
#     print(data["org"])

# auth = HTTPBasicAuth("mlilia", "5810cf49f604f92f9e44a7b128f91dc2705950d7")
# res = requests.get("https://api.github.com/user", auth=auth)

auth = HTTPBasicAuth("mlilia", "bd930c5e7282bd812f80e1f0bb25bd4fcdd75053")
res = requests.get("https://api.github.com/user", auth=auth)

endpoint = "https://api.github.com/gists"
data = {
    "description": "python-hello-world",
    "public": True,
    "files": {
        "hello_world.py": {
            "content": "print(\"Hello World\")"
        }
    }
}

res = requests.post(endpoint, json=data, auth=auth)

print(res.text)
