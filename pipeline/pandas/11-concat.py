#!/usr/bin/env python3

import pandas as pd

from_file = __import__('2-from_file').from_file

# Importing the DataFrame from a CSV file
df1 = from_file('pipeline/pandas/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('pipeline/pandas/data/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# Setting the index of the DataFrame to the 'Timestamp' column
df1.set_index('Timestamp', inplace=True)
df2.set_index('Timestamp', inplace=True)

# Concatenating and adding keys to distinguish between the two DataFrames
df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
# Displaying the concatenated DataFrame
print(df)
