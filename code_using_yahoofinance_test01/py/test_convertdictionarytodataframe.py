# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 13:30:13 2015

@author: justin.malinchak
"""

import pandas

sample={'user1': {'item1': 2.5, 'item2': 3.5, 'item3': 3.0, 'item4': 3.5, 'item5': 2.5, 'item6': 3.0},
        'user2': {'item1': 2.5, 'item2': 3.0, 'item3': 3.5, 'item4': 4.0},
        'user3': {'item2':4.5,'item5':1.0,'item6':4.0}}

df = pandas.DataFrame([
    [col1,col2,col3] for col1, d in sample.items() for col2, col3 in d.items()
])
print df