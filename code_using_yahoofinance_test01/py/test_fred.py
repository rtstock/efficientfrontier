# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:40:17 2015

@author: justin.malinchak
"""
import urllib3
urllib3.disable_warnings()

import fred

# Save your FRED API key.
fred.key('63ef8588c3a78e956fb156c8a1603152')
x = fred.categories(23)
print x
# Interact with economic data categories.

x1 = fred.category()
#print x1
#
x2 = fred.categories(24)
#print x2
#
#fred.children(24)
x3 = fred.children(24)
#print x3
for k,v in x3.items():
    print v[0]
    print v[1]
    
y = fred.related(32073)
#print y
#
z = fred.category(series=True)
print z
#
#fred.category_series(123)
#
#
## Interact with economic data releases.
#fred.releases()
#
#fred.release(250)
#
#fred.dates()
#
#
## Interact with economic data series.
#fred.series('GNPCA')
#
#fred.series('GNPCA', release=True)
#
#fred.observations('AAA')
#
#fred.search('search term')
#
#fred.updates()
#
#fred.vintage('AAA')
#
#
## Query economic data sources.
#fred.sources()
#
#fred.source(23)