#!/usr/bin/env python3

import pandas as pd

from_file = __import__('2-from_file').from_file

# Importing the DataFrame from a CSV file
df = from_file('pipeline/pandas/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

#removing Wighted_Price column
df = df.drop(columns=['Weighted_Price'])

# filling missing values of close column with the previous value
df['Close'] = df['Close'].fillna(method='ffill')
# filling missing values of high, low, open  column with the the equivalent value of close in the same row
df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])
# filling missing values of volume currency and BTC column with 0
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)

print(df.head())
print(df.tail())