import requests
from config import DEBUG


history_buys_endpoint = \
    'https://api.guildwars2.com/v2/commerce/transactions/history/buys'
if DEBUG is True:
    history_buys_endpoint = \
        'http://0.0.0.0:8083/v2/commerce/transactions/history/buy'

items_endpoint = \
    'https://api.guildwars2.com/v2/items'
if DEBUG is True:
    items_endpoint = \
        'http://0.0.0.0:8083/v2/items'


access_token = \
    '44718987-59DC-234C-AEFA-8491368222AF8DD722F7-0A84-4218-B2E8-AD56903D4503'

query_params = {"access_token": access_token}


response_history_buys = requests.get(history_buys_endpoint, query_params)
print(response_history_buys.json())

print()

response_items = requests.get(items_endpoint, {"ids": 94123})
print(response_items.json())
