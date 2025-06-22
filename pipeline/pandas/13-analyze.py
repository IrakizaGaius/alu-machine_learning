#!/usr/bin/env python3

import pandas as pd

from_file = __import__('2-from_file').from_file

# Importing the DataFrame from a CSV file
df = from_file('pipeline/pandas/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
# removing Timestamp column
df.drop(columns=['Timestamp'], inplace=True)

# calculating descriptive statistics for the DataFrame
df = df.describe()
print(df)
