import psycopg2 as pg2
import datetime as datetime
import pandas as pd
import os

# Import csv to DataFrame
df = pd.read_csv('LBMP Compiled.csv', header=0, keep_default_na=False, na_values='.')
format = lambda x: str(x)[:-3]
df['DateOfYear'] = df['Date'].map(format)

#Get Iterables
hours = df.Hour.unique()
zones = df["Zone Name"].unique()
days = df.DateOfYear.unique()

#Compute Averages
records = []
for zone in zones:
    print("zone: " + zone)
    zoneDf = df[df['Zone Name'] == zone]
    for hour in hours:
        #print('Hour:' + str(hour))
        hourDf = zoneDf[zoneDf.Hour == hour]
        for day in days:
            #print('day:' + day)
            records.append({  'Date':day,
                              'Hour':hour,
                              'Zone':zone,
                              'LBMP Mean':hourDf[hourDf.DateOfYear == day].LBMP.mean()})

# Throw Averages into DataFrame            
allAveragesDf = pd.DataFrame(records)

format = lambda x: '%.2f' % x
allAveragesDf['LBMP Mean'] = allAveragesDf['LBMP Mean'].map(format)

#Single Average Query
#allAveragesDf[(allAveragesDf["Date"] == '1/1') & (allAveragesDf["Hour"] == 1) & (allAveragesDf["Zone"] == 'CAPITL')]

# Export to CSV
folder = os.getcwd()
csvPath = os.path.join(folder, 'AveragedData.csv')
allAveragesDf.to_csv(path_or_buf=csvPath)