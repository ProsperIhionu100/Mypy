import json 
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/currencies") as response:
    source = response.read()
#print(source)

data = json.loads(source)

print(json.dumps(data,indent=2))