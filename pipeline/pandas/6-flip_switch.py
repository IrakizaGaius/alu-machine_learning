#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('pipeline/pandas/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# sorting data in chronological order
df = df.sort_index(ascending=False)
# Flipping the DataFrame to switch rows and columns
df = df.T

print(df.tail(8))
