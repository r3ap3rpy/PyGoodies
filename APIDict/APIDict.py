try:
    import requests
except:
    raise SystemExit("Please: pip install requests")

from collections.abc import MutableMapping
from json import loads

class APIDict(MutableMapping):
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def __getitem__(self, key):
        return loads(requests.get(url = f"{self.endpoint}/get?key={key}").text)

    def __setitem__(self, key, value):
        requests.post(url = f"{self.endpoint}/set?key={key}&value={value}")

    def __delitem__(self, key):
        requests.post(url = f"{self.endpoint}/del?key={key}")

    def __len__(self):
        return len(loads(requests.get(url = f"{self.endpoint}").text))
    
    def __iter__(self):
        return iter(loads(requests.get(url = f"{self.endpoint}").text).items())
    def __repr__(self):
        return f"APIDict(endpoint = {self.endpoint})"
    

if __name__ == '__main__':
    ad = APIDict(endpoint="http://192.168.50.145:8000")
    ad['a'] = 10
    ad['b'] = 20
    print(ad['a'])
    for item in iter(ad):
        print(item)