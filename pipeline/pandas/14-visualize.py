#!/usr/bin/env python3

import pandas as pd

from_file = __import__('2-from_file').from_file

# Importing the DataFrame from a CSV file
df = from_file('pipeline/pandas/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
# removing Weighted_price column
df.drop(columns=['Weighted_Price'], inplace=True)
# renaming Timestamp column to Date
df.rename(columns={'Timestamp': 'Date'}, inplace=True)
# Convert "Date" to datetime
df['Date'] = pd.to_datetime(df['Date'], unit='s')
# Indexing on Date
df.set_index('Date', inplace=True)
# filling missing values in 'Close' column with previous values
df['Close'].fillna(method='ffill', inplace=True)
# filling missing values in 'High', 'Low', 'Open' columns with the equivalent value of 'Close' in the same row
df['High'].fillna(df['Close'], inplace=True)
df['Low'].fillna(df['Close'], inplace=True)
df['Open'].fillna(df['Close'], inplace=True)
# filling missing values in 'Volume_(Currency)' and 'Volume_(BTC)' columns with 0
df['Volume_(Currency)'].fillna(0, inplace=True)
df['Volume_(BTC)'].fillna(0, inplace=True)
# Visualizing the DataFrame from data from 2017 and beyond at daily intervals and group the values of the same day such that: 
# High: max
# Low: min
# Open: mean
# Close: mean
# Volume(BTC): sum
# Volume(Currency): sum
df = df.loc['2017-01-01':]
df = df.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})
# plotting the DataFrame
df.plot(title='Coinbase USD Prices', figsize=(12, 6))
# Show the plot
import matplotlib.pyplot as plt
plt.show()