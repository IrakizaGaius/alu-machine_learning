#!/usr/bin/env python3
"""Defines multiple neurons performing binary classification"""
import numpy as np


class NeuralNetwork:
    """Class NeuralNetwork that defines a neural network
    performing binary classification"""
    def __init__(self, nx, nodes):
        """Constructor of the class NeuralNetwork
        Args:
            nx (int): number of input features to the neuron
            nodes (int): number of nodes in the hidden layer
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx <= 0:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes <= 0:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """Getter for W1"""
        return self.__W1

    @property
    def b1(self):
        """Getter for b1"""
        return self.__b1

    @property
    def A1(self):
        """Getter for A1"""
        return self.__A1

    @property
    def W2(self):
        """Getter for W2"""
        return self.__W2

    @property
    def b2(self):
        """Getter for b2"""
        return self.__b2

    @property
    def A2(self):
        """Getter for A2"""
        return self.__A2

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network
        Args:
            X (ndarray): input data of shape (nx, m)
        Returns:
            A1 (ndarray): output of the hidden layer
            A2 (ndarray): output of the network
        """
        Z1 = np.dot(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-Z1))
        Z2 = np.dot(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-Z2))
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression
        Args:
            Y (ndarray): correct labels for the input data
            A (ndarray): activated output of the neuron for each example
        Returns:
            cost (float): cost of the model
        """
        a = (Y * np.log(A))
        b = ((1 - Y) * np.log(1.0000001 - (A)))
        sigma = a + b
        return (-1 / Y.shape[1]) * np.sum(sigma)
