#!usr/bin/env python3
"""Creating a pandas dataframe from a numpy array"""

def from_numpy(array):
    """Function that takes in a numpy array and creates a Pandas dataframe from it"""
    import pandas as pd
    return pd.DataFrame(array)
