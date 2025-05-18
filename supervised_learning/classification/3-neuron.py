#!/usr/bin/env python3
"""Defines a single neuron performing binary classification"""
import numpy as np


class Neuron:
    """Class Neuron that defines a single neuron
performing binary classification"""
    def __init__(self, nx):
        """Constructor of the class Neuron
        Args:
            nx (int): number of input features to the neuron
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx <= 0:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for W"""
        return self.__W

    @property
    def b(self):
        """Getter for b"""
        return self.__b

    @property
    def A(self):
        """Getter for A"""
        return self.__A

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron
        Args:
            X (numpy.ndarray): input data of shape (nx, m)
                nx: number of input features
                m: number of examples
        Returns:
            A (numpy.ndarray): activated output of the neuron
        """
        z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-z))
        return self.__A

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression
        Args:
            Y (numpy.ndarray): correct labels for the input data
                shape (1, m)
            A (numpy.ndarray): activated output of the neuron
                shape (1, m)
        Returns:
            cost (float): cost of the model
        """
        a = (Y * np.log(A))
        b = ((1 - Y) * np.log(1.0000001 - A))
        sigma = a + b
        return (- 1 / Y.shape[1]) * np.sum(sigma)
