#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Importing the DataFrame from a CSV file
df = from_file('pipeline/pandas/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Sorting by Highest price
df = df.sort_values(by='Weighted_Price', ascending=False)
# Flipping the DataFrame to switch rows and columns
print(df.head())