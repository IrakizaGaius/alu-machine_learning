#!/usr/bin/env python3

"""
This module provides a function to calculate the correlation matrix
from a given covariance matrix.

The correlation matrix is computed using the formula:
corr_matrix(i, j) = cov(i, j) / (std_devs[i] * std_devs[j])

Where:
- cov(i, j) is the covariance between variables i and j.
- std_devs[i] is the standard deviation of variable i.
"""

import numpy as np


def correlation(C):
    """
    Calculate the correlation matrix from a covariance matrix.

    The function takes a square covariance matrix as input and returns the
    correlation matrix by normalizing the covariance matrix with the standard
    deviations of the variables.

    Args:
        C (numpy.ndarray): A square covariance matrix (2D numpy array).

    Returns:
        numpy.ndarray: A square correlation matrix where each element is
        the correlation between two variables.

    Raises:
        TypeError: If the input matrix is not a numpy.ndarray.
        ValueError: If the input matrix is not square (not of shape (n, n)).
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
