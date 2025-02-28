#!/usr/bin/env python3
"""
This module provides a function to compute the mean and covariance matrix
of a dataset.

The mean is calculated as the average of the data points along each dimension.
The covariance matrix is calculated using the formula:

cov(i, j) = sum((X_i - mean_i) * (X_j - mean_j)) / (n - 1)

Where:
- X_i is the data in the ith dimension.
- mean_i is the mean of the ith dimension.
- n is the number of data points.
"""

import numpy as np


def mean_cov(X):

    """
    Calculate the mean and covariance matrix of a dataset.

    This function computes the mean and covariance of the input data X, which
    is expected to be a 2D numpy array where each row is a data point and
    each column corresponds to a feature (dimension).

    Args:
        X (numpy.ndarray): A 2D numpy array with shape (n, d), where n is the
    number of data points and d is the number of dimensions
                           (features).

    Returns:
    tuple: A tuple containing:
    - mean (numpy.ndarray): A 1D numpy array of shape (d,) representing the
    mean of the data points along each dimension.
    - cov (numpy.ndarray): A 2D numpy array of shape (d, d) representing the
    covariance matrix of the data.

    Raises:
        TypeError: If the input is not a 2D numpy.ndarray.
        ValueError: If the input contains fewer than 2 data points.
    """

    # Check that the input is a 2D numpy array
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    # Ensure there are multiple data points
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate the mean along each dimension (axis 0)
    mean = np.mean(X, axis=0).reshape(1, d)

    # Calculate the covariance matrix using the formula
    cov = np.dot((X - mean).T, (X - mean)) / (n - 1)

    return mean, cov
