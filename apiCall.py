import requests
import json
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc':'012993441012'} # <-- change this number barcode
response = requests.get(baseUrl, params=parameters)

# testing response
# print(response.url)

# parsing through JSON
content = response.content
info = json.loads(content) #change json to dict

item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print('name : ',title)
print('brand : ',brand)

