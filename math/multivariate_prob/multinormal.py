#!/usr/bin/env python3
"""MULTIVARIATE PROBABILITY DISTRIBUTIONS"""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal Distribution"""

    def __init__(self, data):
        """Initialize the MultiNormal instance"""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)  # Mean vector (d, 1)
        self.cov = (data - self.mean) @ (data - self.mean).T / (n - 1)

    def pdf(self, x):
        """Calculate the PDF at a data point"""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d, _ = self.mean.shape
        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det = np.linalg.det(self.cov)
        if det <= 1e-10:
            raise ValueError("covariance matrix is nearly singular")

        inv_cov = np.linalg.inv(self.cov)

        diff = x - self.mean
        exponent = -0.5 * (diff.T @ inv_cov @ diff).item()

        norm = 1 / np.sqrt(((2 * np.pi) ** d) * det)

        pdf = float(norm * np.exp(exponent))

        return pdf
