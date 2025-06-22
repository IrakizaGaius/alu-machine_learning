#!/usr/bin/env python3

import pandas as pd

from_file = __import__('2-from_file').from_file

# Importing the DataFrame from a CSV file
df1 = from_file('pipeline/pandas/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('pipeline/pandas/data/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# Setting the index of the DataFrame to the 'Timestamp' column
df1.set_index('Timestamp', inplace=True)
df2.set_index('Timestamp', inplace=True)
#!/usr/bin/env python3

import pandas as pd

from_file = __import__('2-from_file').from_file

# Importing the DataFrame from a CSV file
df1 = from_file('pipeline/pandas/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('pipeline/pandas/data/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# Step 1: Set index for both DataFrames
df1.set_index('Timestamp', inplace=True)  # bitstamp
df2.set_index('Timestamp', inplace=True)  # coinbase

# Step 2: Filter the desired timestamp range
start, end = 1417411980, 1417417980
df1 = df1.loc[start:end]
df2 = df2.loc[start:end]

# Step 3: Add exchange column to each
df1['exchange'] = 'bitstamp'
df2['exchange'] = 'coinbase'

# Step 4: Combine the two
df = pd.concat([df1, df2])

# Step 5: Set MultiIndex: (Timestamp, exchange)
df.set_index('exchange', append=True, inplace=True)
df.index.names = ['timestamp', '']

# Step 6: Sort so rows group nicely
df.sort_index(inplace=True)

# Displaying the concatenated DataFrame
print(df)