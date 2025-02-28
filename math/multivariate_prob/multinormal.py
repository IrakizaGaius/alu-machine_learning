##!/usr/bin/env python3
"""Multinormal class to represent a Multivariate Normal Distribution"""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal Distribution"""

    def __init__(self, data):
        """Initialize the MultiNormal instance"""
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Mean vector (d, 1)
        self.mean = np.mean(data, axis=1, keepdims=True)
        # Covariance matrix (d, d)
        self.cov = (data - self.mean) @ (data - self.mean).T / (n - 1)

    def pdf(self, x):
        """Calculate the PDF at a data point"""
        # Ensure x is a numpy array
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        # Ensure x has the correct shape (d, 1)
        d, _ = self.mean.shape
        if x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")

        # Compute determinant of covariance matrix with stability check
        det = np.linalg.det(self.cov)
        if det <= 1e-10:  # Avoid singular matrix issues
            raise ValueError("covariance matrix is nearly singular")

        # Compute inverse of covariance matrix
        inv_cov = np.linalg.inv(self.cov)

        # Compute the exponent term in the PDF
        diff = x - self.mean
        exponent = -0.5 * (diff.T @ inv_cov @ diff).item()  # Scalar value

        # Compute the normalization term
        norm = 1 / np.sqrt(((2 * np.pi) ** d) * det)

        # Compute PDF with float64 precision
        pdf = float(norm * np.exp(exponent))

        return pdf
