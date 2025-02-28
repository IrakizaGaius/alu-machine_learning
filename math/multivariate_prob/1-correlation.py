#!/usr/bin/env python3

import numpy as np

"""Function correlation."""


def correlation(C):
    """
    Calculates a correlation matrix
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    diag = np.diag(np.sqrt(np.diag(C)))
    inv = np.linalg.inv(diag)
    corr = np.dot(np.dot(diag, C), inv)
    return corr
