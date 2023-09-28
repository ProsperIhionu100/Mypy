import json

mydict = {
    "people":[
        {
            "name":"Bob", 
            "age" : 28,
            "weight":80
        },
        {
            "name":"Anna",
            "age" : 34,
            "weight":67
        },
        {
            "name":"Charles",
            "age" : 45,
            "weight":78
        },
        {
            "name":"Daneil",
            "age" : 21,
            "weight":110
        }
    ]
}

json_string = json.dumps(mydict, indent=1)
with open("mydata.json","w") as f:
    f.write(json_string)