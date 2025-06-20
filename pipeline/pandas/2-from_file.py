#!/usr/bin/env python3
"""Create a pandas DataFrame from a CSV file."""
import pandas as pd

def from_file(filename, delimiter):
    df = pd.read_csv(filename, delimiter=delimiter)
    return df
