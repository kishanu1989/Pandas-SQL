import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

airport_freq = pd.read_csv(
    'C:/Users/kibhattacharya/Desktop/GoTo Docs/ML/DataSets/Airport Frequency/airport-frequencies.csv')
airport = pd.read_csv(
    'C:/Users/kibhattacharya/Desktop/GoTo Docs/ML/DataSets/Airport Frequency/airports.csv')
runways = pd.read_csv(
    'C:/Users/kibhattacharya/Desktop/GoTo Docs/ML/DataSets/Airport Frequency/runways.csv')

print(airport)  # select * from airport
print(airport.head())  # select * from airport limit -5
print(airport[airport.ident == 'KLAX'].id)  # select id from airport where ident = 'KLAX'
print(airport.type.unique())  # select distinct type from airport

# select * from airport where iso_region = 'US-CA' and type = 'seaplane_base'
print(airport[(airport.iso_region == 'US-CA') & (airport.type == 'seaplane_base')])

# select ident,name,municipality from airport where iso_region = 'US-CA' and type = 'seaplane_base'
print(airport[(airport.iso_region == 'US-CA') & (airport.type == 'seaplane_base')][['ident', 'name', 'municipality']])

# select ident,name,municipality from airport where iso_region = 'US-CA' and type = 'seaplane_base' order by municipality
print(airport[(airport.iso_region == 'US-CA') & (airport.type == 'seaplane_base')].sort_values('municipality',
                                                                                               ascending=False)[
          ['ident', 'name', 'municipality']])

# In and NotIn
# select * from airports where type in ('heliport', 'balloonport')
print(airport[airport.type.isin(['seaplane_base', 'balloonport'])])

# Not IN
print(airport[~airport.type.isin(['seaplane_base', 'balloonport'])])

# select iso_country, type, count(*) from airports group by iso_country, type order by iso_country, type
print(airport.groupby(['iso_country', 'type']).size())

# select iso_country, type, count(*) from airports group by iso_country, type order by iso_country, count(*) desc
# to_frame() : this is used to sort the frame using the calculated field. and once the group by is done, the frame structure changes
# reset_index(): As the frame size changes, to reset it and restart it again we use reset_index()
print(
    airport.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'],
                                                                                                ascending=[True,
                                                                                                           False]))
# Groupby using Having
print(airport[airport.iso_country == 'US'].groupby('type').filter(lambda g: len(g) > 1000).groupby(
    'type').size().sort_values(ascending=False))

# Top N Records
print(runways.head(3))

# Aggregate Functions MIN, MAX, MEAN
# select max(length_ft), min(length_ft), mean(length_ft), median(length_ft) from runways
# .T is used to do the transpose. To see it run the below query without using and then using it.
print(runways.agg({'length_ft': ['min', 'max', 'mean', 'median']}).T)
# OR the describe function can be used for the column.
print(runways['length_ft'].describe())

# Joins
# select airport_ident, type, description, frequency_mhz
# from airport_freq join airports on airport_freq.airport_ref = airports.id
# where airports.ident = 'KLAX'
print(airport_freq.merge(airport[airport.ident == 'KLAX'][['id']], left_on='airport_ref', right_on='id', how='inner')[
          ['airport_ident', 'type', 'description', 'frequency_mhz']])

#Union and Union All
#Use pd.concat([dataframe1,dataframe2])

#Drop duplicates
#pd.drop_duplicates()

#Create a Dataframe
df1 = pd.DataFrame({'id':[],'name':[]})
#Insert records
df1 = pd.DataFrame({'id':[1],'name':['Jack']})

#Update in the Dataframe
#update airports set home_link = 'http://www.lawa.org/welcomelax.aspx' where ident == 'KLAX'
airport.loc[airport['ident'] == 'KLAX', 'home_link'] = 'abcd'