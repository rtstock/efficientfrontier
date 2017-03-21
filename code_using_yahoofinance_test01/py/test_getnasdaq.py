"""
GET http://ws.nasdaqdod.com/v1/NASDAQQuotes.asmx/GetQuotes?
Symbols=string&StartDateTime=string&EndDateTime=string&MarketCenters=string
     HTTP/1.1
Host: ws.nasdaqdod.com

"""

#url = 'http://ws.nasdaqdod.com/v1/NASDAQQuotes.asmx/GetQuotes?Symbols=aaplStartDateTime=string&EndDateTime=string&MarketCenters=string

url = 'http://ws.nasdaqdod.com/v1/NASDAQQuotes.asmx/GetQuotes?Symbols=NDAQ&StartDateTime=8/12/2016 09:30:00.000&EndDateTime=8/12/2016 09:30:25.000&MarketCenters=Q, B'


import requests
r = requests.get(url)

print r.status_code
print r.headers
print r.content
