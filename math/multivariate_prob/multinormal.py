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

    def pdf(self, x):
        """Calculate the value of the PDF at a data point"""
        # Check if the input data is a 2D numpy.ndarray
        if not isinstance(x, np.ndarray) or len(x.shape) != 2:
            raise TypeError("x must be a 2D numpy.ndarray")
        
        # Get the number of dimensions (d) and number of data points (n)
        d, n = x.shape

        # Check if the dimensions of x match the dimensions of the data
        if d != self.mean.shape[0]:
            raise ValueError("x must have the shape ({d}, 1)")

        # Compute the determinant of the covariance matrix
        det = np.linalg.det(self.cov)

        # Check if the covariance matrix is singular
        if det == 0:
            raise ValueError("cov cannot be singular")

        # Compute the inverse of the covariance matrix
        inv_cov = np.linalg.inv(self.cov)

        # Compute the exponent term in the PDF
        diff = x - self.mean
        exponent = -0.5 * np.sum(np.dot(diff.T, inv_cov) * diff.T, axis=1)

        # Compute the normalization term
        norm = 1 / np.sqrt((2 * np.pi) ** d * det)

        # Compute the PDF
        pdf = norm * np.exp(exponent)
        return pdf
