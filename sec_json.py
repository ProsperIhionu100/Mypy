import json

with open("mydata.json","r") as f:
    json_object = json.loads(f.read())
    
for item in json_object['people']:
    print(item['name'])