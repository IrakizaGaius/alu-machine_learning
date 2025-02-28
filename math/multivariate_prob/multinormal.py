#!/usr/bin/env python3
"""MultiNormal class"""
import numpy as np


class MultiNormal:
    """Multi
    Normal class"""
    def __init__(self, data):
        """Constructor"""
        # Check if the input data is a 2D numpy.ndarray
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        # Get the number of dimensions (d) and number of data points (n)
        d, n = data.shape

        # Check if n (number of data points) is less than 2
        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Compute the mean

        self.mean = np.mean(data, axis=1, keepdims=True)

        # Compute the covariance matrix
        # Subtract the mean from the data points
        data_centered = data - self.mean
        self.cov = np.dot(data_centered, data_centered.T) / (n - 1)
