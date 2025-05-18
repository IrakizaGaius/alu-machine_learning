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
        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0
