#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:42:41 2017

@author: shannnonliburd
"""

import psycopg2 as pg2
import datetime as datetime
import pandas as pd


def dateString(date):
    return date.strftime("%Y-%m-%d")

conn=pg2.connect(database='energy', user = 'postgres', password='input')
cur=conn.cursor()
cur.execute("SELECT * FROM compiled")
data=cur.fetchall()
dataf=[{'id':record[0], 'date':record[1], 'hour':record[2], 'zone':record[3],'lbmp':record[4]} for record in data]
df=pd.DataFrame(dataf)




#zones=['CAPITL','CENTRL','DUNWOD', 'GENESE','H Q', 'HUD VL', 'LONGIL', 'MHK VL', 'MILLWD', 'N.Y.C.', 'NORTH', 'NPX', 'O H', 'PJM', 'WEST']
#
#for hour in range(24):
#    for zone in zones:
#        
#        d0=datetime.datetime.strptime('01-01-2014','%d-%m-%Y')
#        d1=datetime.datetime.strptime('01-01-2015','%d-%m-%Y')
#        d2=datetime.datetime.strptime('01-01-2016','%d-%m-%Y')
#        d3=datetime.datetime.strptime('01-01-2017','%d-%m-%Y')
#
#        for day in range(365):
#          date=[dateString(d0+datetime.timedelta(days=day)),dateString(d1+datetime.timedelta(days=day)),dateString(d2+datetime.timedelta(days=day)),dateString(d3+datetime.timedelta(days=day))]
#          print(date)
#          cur.execute("SELECT zone_name, ROUND(AVG(lbmp),2) AS avg FROM compiled WHERE zone_name= %s AND hour=%s AND date IN(%s,%s, %s,%s) GROUP BY zone_name;",(zone,hour,date[0],date[1],date[2],date[3]))
#          print(cur.fetchone())
#
#        
