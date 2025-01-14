import requests

endpoint="http://127.0.0.1:8000/api/"
response=requests.get(endpoint,params={"abc":123})
print(response.text)
print(response.json())