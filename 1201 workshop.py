# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:02:48 2023

@author: a2268
"""

# Coding Task 0 - Day 2

# Following is the data for 3 shops stating the amount of cars sold each week

shop1 = {'Week1': {'BMW': 5, 'Porsche': 1, 'VW': 2},
         'Week2': {'BMW': 1, 'Porsche': 5, 'VW': 10},
         'Week3': {'BMW': 5, 'Porsche': 4, 'VW': 13},
         'Week4': {'BMW': 15, 'Porsche': 11, 'VW': 2},
         }

shop2 = {'Week1': {'BMW': 1, 'Porsche': 10, 'VW': 3},
         'Week2': {'BMW': 10, 'Porsche': 5, 'VW': 7},
         'Week3': {'BMW': 8, 'Porsche': 4, 'VW': 3},
         'Week4': {'BMW': 15, 'Porsche': 1, 'VW': 6},
         }


shop3 = {'Week1': {'BMW': 3, 'Porsche': 2, 'VW': 6},
         'Week2': {'BMW': 7, 'Porsche': 2, 'VW': 1},
         'Week3': {'BMW': 5, 'Porsche': 6, 'VW': 8},
         'Week4': {'BMW': 4, 'Porsche': 5, 'VW': 2},
         }

shop4 = {'Week1': {'BMW': 5, 'Porsche': 2, 'VW': 6},
         'Week2': {'BMW': 7, 'Porsche': 1, 'VW': 11},
         'Week3': {'BMW': 5, 'Porsche': 1, 'VW': 8},
         'Week4': {'BMW': 1, 'Porsche': 5, 'VW': 0},
         }

car_sales_data_list = [shop1, shop2, shop3, shop4]


'''
Task 1 : Count the total number of cars sold (per car) in all shops, in 4 weeks.


Task 2 : Find the most sold car

'''
count_BMW = 0
count_Por = 0
count_VW = 0
for shops in car_sales_data_list:
    for weeks in shops:
        count_BMW = count_BMW + shops[weeks]['BMW']
        count_Por = count_Por + shops[weeks]['Porsche']
        count_VW = count_VW + shops[weeks]['VW']

print(max(count_BMW, count_Por, count_VW))

import os
path = os.getcwd()
print(path)

os.chdir('C:\\Users\\a2268\\OneDrive\\桌面\\Random stuff\\Python workshop')

import pandas as pd
df_car_sales_data = pd.read_excel("C:\\Users\\a2268\\OneDrive\\桌面\\Random stuff\\Python workshop\\car_sales.xlsx")
df_car_sales_data['BMW'].sum()

df_car_sales_data.describe()
df_car_sales_data.info()

df_shop1 = df_car_sales_data.query("ShopName == 'shop1'")
df_week1 = df_car_sales_data.query("Week == 'Week1'")

df_car_sales_data.query("BMW > 5")

# Save to an excel file
df_shop1.to_excel('shop1.xlsx', index = False)

Week1_Porsche = df_car_sales_data.query("Week == 'Week1'")['Porsche'].sum()


# Create a dataframe
data = {
        'Apples':[3,2,0,1],
        'Oranges': [0,3,7,2]
        }

df_purchases = pd.DataFrame(data)

data_2 = {
        'A':[3,2,0,1]
        }

df = pd.DataFrame(data_2)

df_series = df_purchases['Apples'] # Series

df_purchases.info()
df_purchases.dtypes
df_purchases.max()

name_dict = {0:"Klaus", 1:"Hans",2:"Anna",3:"Lena"}
df_purchases = df_purchases.rename(index = name_dict)

name_list = ['Klaus','Hans','Anna','Lena']
df_purchases2 = pd.DataFrame(data, index = name_list)
df_purchases2['Fruit'] = [5,8,9,5]

df_append = pd.concat([df_purchases,df_purchases2], axis = 1)

df_append.columns = df_append.columns.str.upper()

'''
Task
'''
df_new = {
    'Kiwi': [0,1,2,3],
    'Strawberry':[5,6,7,8]
    }
df_new = pd.DataFrame(df_new, index = ['Klaus','Hans','Anna','Lena'])
df_concat = pd.concat([df_purchases2,df_new],axis = 1)

df_drop = df_append.drop('FRUIT', axis = 1)
df_drop = df_append.drop('Lena')

# Covid data
import pandas as pd

df_covid = pd.read_csv('owid-covid-data.csv')
df_covid.describe()
df_covid.info()
df_covid_de = df_covid.query("location =='Germany'")
df_covid_sample = df_covid.head(100)

df_covid_location = df_covid['location'].drop_duplicates()

df_covid_issue = df_covid.query('new_deaths < 0' )

df_covid_de_new_cases = df_covid_de[['location', 'date', 'new_cases']]
df_covid_de_new_cases.plot(x = 'date', y = 'new_cases')
df_covid_de_new_cases.max()
df_covid_de_new_cases.dtypes

df_covid_de_new_cases['date2'] = pd.to_datetime(df_covid_de_new_cases['date'])

df_by_month = df_covid_de_new_cases.resample('M', on = 'date2').sum()
df_by_month.plot()

import matplotlib.pyplot as plt











