#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('pipeline/pandas/data/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# YOUR CODE HERE
df.rename(columns = { 'Timestamp': 'DateTime',}, inplace=True)
# Convert "timestamp" to datetime
df['DateTime'] = pd.to_datetime(df['DateTime'], unit='s')
# display only Datetime and Close columns
df = df[['DateTime', 'Close']]
print(df.tail())