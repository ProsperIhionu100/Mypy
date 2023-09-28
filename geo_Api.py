import requests 
import pandas as pd

base_url = "https://rickandmortyapi.com/api/"
endpoint = 'character'

def main_request(base_url, endpoint, x):
    r = requests.get(base_url + endpoint + f'?page={x}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist = []
    for item in response['results']:
        char= {
            'id': item['id'],
            'name': item['name'],
            'no_ep': len(item['episode'])
        }
        charlist.append(char)
    return charlist
    
#print(r.json())
mainlist = []
data = main_request(base_url, endpoint,1)
for x in range(1,get_pages(data)+1): 
    print(x)
    mainlist.extend(parse_json(main_request(base_url, endpoint,x)))
    
df =  pd.DataFrame(mainlist)
#print(df.head(), df.tail())
df.to_csv('charlist.csv', index=False)