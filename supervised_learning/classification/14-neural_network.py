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

    def evaluate(self, X, Y):
        """Evaluates the neural network's predictions
        Args:
            X (ndarray): input data of shape (nx, m)
            Y (ndarray): correct labels for the input data
        Returns:
            A (ndarray): predicted labels
            cost (float): cost of the model
        """
        self.forward_prop(X)
        A = np.where(self.__A2 >= 0.5, 1, 0)
        cost = self.cost(Y, self.__A2)
        return A, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """Calculates one pass of gradient descent on the neural network
        Args:
            X (ndarray): input data of shape (nx, m)
            Y (ndarray): correct labels for the input data
            A1 (ndarray): output of the hidden layer
            A2 (ndarray): output of the network
            alpha (float): learning rate
        """
        m = Y.shape[1]
        dZ2 = A2 - Y
        dW2 = np.dot(dZ2, A1.T) / m
        db2 = np.sum(dZ2, axis=1, keepdims=True) / m
        dZ1 = np.dot(self.__W2.T, dZ2) * (A1 * (1 - A1))
        dW1 = np.dot(dZ1, X.T) / m
        db1 = np.sum(dZ1, axis=1, keepdims=True) / m

        self.__W2 -= alpha * dW2
        self.__b2 -= alpha * db2
        self.__W1 -= alpha * dW1
        self.__b1 -= alpha * db1

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """Trains the neural network
        Args:
            X (ndarray): input data of shape (nx, m)
            Y (ndarray): correct labels for the input data
            iterations (int): number of iterations to train
            alpha (float): learning rate
        Returns:
            A (ndarray): output of the neural network after training
            cost (float): cost of the model after training
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha)

        return self.evaluate(X, Y)
