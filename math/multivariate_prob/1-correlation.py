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

    # Get the standard deviations (square root of the diagonal elements of C)
    std_devs = np.sqrt(np.diag(C))
    # Calculate the correlation matrix
    corr_matrix = C / (std_devs[:, None] * std_devs[None, :])

    return corr_matrix
