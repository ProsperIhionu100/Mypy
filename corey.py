import json 

people_String = '''
{
    "people":[
        {
            "name": "John Smith",
            "Phone": "08033965437",
            "emails": ["johnsmith@bogusemail.com","johnsmith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Smith",
            "Phone": "08179341114",
            "emails": null,
            "has_license": true
            }   
        ]

}'''

data = json.loads(people_String)
# print(type(data["people"])) 

for person in data['people']:
    #print(person['name'])
    del person['Phone']
    
new_string = json.dumps(data, indent=2,sort_keys=True)
print(new_string)   