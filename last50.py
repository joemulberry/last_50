import requests
import json 
from time import time

''''
dict_keys(['approved_account', 
'asset', 'asset_bundle', 
'auction_type', 'bid_amount', 
'collection_slug', 
'contract_address', 
'created_date', 
'custom_event_name', 
'dev_fee_payment_event', 
'duration', 
'ending_price', 
'event_type', 
'from_account', 
'id', 
'owner_account', 
'payment_token', 
'quantity',
'seller', 
'starting_price', 
'to_account', 
'total_price', 
'transaction', 
'winner_account'])
'''

url = "https://api.opensea.io/api/v1/events"
querystring = {"asset_contract_address":"0x76be3b62873462d2142405439777e971754e8e77","event_type":"successful","only_opensea":"false","offset":"0","limit":"50"}
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
events = data['asset_events']

print(events[0].keys())

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

print(di)

# for d in os_data:

#     if d['last_sale'] != None:
#         if d['last_sale']['payment_token']['symbol'] == 'ETH':
#             eth += 1
#         else:
#             not_eth += 1

# total_count = not_eth+eth
# print((eth, not_eth, total_count))

# eth = eth / total_count
# not_eth = not_eth / total_count

# eth = round(eth, 2)
# not_eth = round(not_eth, 2)

# di = {
#     'a': eth,
#     'b': not_eth,
#     't': time()
# }

# w_or_e_data.append(di)

# print(w_or_e_data)

# with open('ask_bids.json', 'w') as fout:
#     json.dump(w_or_e_data, fout)

# with open('ask_bids_now.json', 'w') as fout:
#     json.dump([di], fout)
