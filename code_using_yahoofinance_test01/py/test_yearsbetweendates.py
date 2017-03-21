# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:11:35 2015

@author: justin.malinchak
"""


import datetime
time1 =   datetime.datetime.strptime("2011-08-07 16:00", "%Y-%m-%d %H:%M")
time2 = datetime.datetime.now() # waited a few minutes before pressing enter
elapsedTime = time2 - time1
#print elapsedTime
#datetime.timedelta(0, 125, 749430)
#print divmod(elapsedTime.total_seconds(), 60)[0]
#print divmod(elapsedTime.total_seconds(), 60.0)[0]/60.0/24.0/365.0
yrs = divmod(elapsedTime.total_seconds(), 60.0)[0]/60.0/24.0/365.0
#print yrs

#(2.0, 5.749430000000004) # divmod returns quotient and remainder
# 2 minutes, 5.74943 seconds


