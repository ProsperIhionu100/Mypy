import json

with open("my_states.json") as fh:
    json_read =json.load(fh)

for item in json_read['states']:
    read_file = (item["name"],item["abbreviation"])
    
with open("other_file.json", "w") as f:
    rd =json.dumps(read_file)
    f.write(rd)