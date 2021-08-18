import requests
import json 
from time import time

url = "https://api.opensea.io/api/v1/events"
querystring = {"asset_contract_address":"0x76be3b62873462d2142405439777e971754e8e77","event_type":"successful","only_opensea":"false","offset":"0","limit":"50"}
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
events = data['asset_events']

url = 'https://raw.githubusercontent.com/joemulberry/last_50/main/last50.json'
resp = requests.get(url)
last50_data = json.loads(resp.text)

eth = 0
not_eth = 0

for event in events:
    if event['payment_token']['symbol'] == 'ETH':
        eth += 1
    else:
        not_eth += 1   

total_count = not_eth+eth

eth = eth / total_count
not_eth = not_eth / total_count

eth = round(eth, 2)
not_eth = round(not_eth, 2)

di = {
    'a': eth,
    'b': not_eth,
    't': time()
    }

last50_data.append(di)

with open('last50.json', 'w') as fout:
    json.dump(last50_data, fout)

with open('last50_now.json', 'w') as fout:
    json.dump([di], fout)