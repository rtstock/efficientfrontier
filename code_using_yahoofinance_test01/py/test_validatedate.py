# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 10:14:28 2015

@author: justin.malinchak
"""

import datetime
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False
        
        
print validate_date('2014-01-')