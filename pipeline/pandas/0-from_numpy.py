#!/usr/bin/env python3
"""Creating a pandas DataFrame from a numpy array with alphabetical column labels"""

def from_numpy(array):
    """
    Function that takes in a numpy array and creates a Pandas DataFrame from it.
    The DataFrame columns are labeled with capitalized alphabetical letters (A-Z).
    """
    import pandas as pd
    import string

    num_cols = array.shape[1]
    if num_cols > 26:
        raise ValueError("Array cannot have more than 26 columns for alphabetical labeling.")

    col_labels = list(string.ascii_uppercase[:num_cols])
    return pd.DataFrame(array, columns=col_labels)
