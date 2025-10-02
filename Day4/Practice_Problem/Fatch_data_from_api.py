import requests
import json
data = requests.get("https://jsonplaceholder.typicode.com/todos")
json_data = data.json()

print(json_data,end="\n")
print(data)
