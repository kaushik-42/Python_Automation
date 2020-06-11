import requests
import json
#WE ARE USING A UPC UTEM API WHERE IT WILL GIVE OUT RELEVANT INFORMATION ABOUT THE PRODUCT YOU WANTED!
baseurl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '0012993441012'}
#UPC IS A UNIQUE BARCODE NO WHERE IT WILL SEND YOU ALL THE RELATIVE INFORMATION
#THAT KNOWS ABOUT THE BAR CODE!
response = requests.get(baseurl, params=parameters)
# print(response.url)
content = response.content
info = json.loads(content)
# print(type(info))
# print(info)
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)
