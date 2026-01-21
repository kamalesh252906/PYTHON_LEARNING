# import json

# student =  '{"name" : "Alex","age" : 25,"isStudent": true,"skills": ["python","SQL"],"address" : {"city":"Mumbai","pin code" : 400001 }}'
# a = json.dumps(student)
# print(a)
# print(type(a))
# print(a["address"]["city"])
# print(a["skills"][1])
# b = json.loads(student)
# print(b)
# print(type(b))

import json
import requests
# Step 1: Make a GET request to the API
response = requests.get("https://randomuser.me/api/")
# Step 2: Convert response JSON → Python dict
data = response.json()
# Step 3: Extract some values
user = data["results"][0]
name = user["name"]["first"]
email = user["email"]
city = user["location"]["city"]
print("Name:", name)
print("Email:", email)
print("City:", city)

