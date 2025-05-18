#!/usr/bin/env python3
"""Defines a deep neural network for binary classification."""
import numpy as np


class DeepNeuralNetwork:
    """Deep neural network for binary classification.

    Attributes:
        nx (int): Number of input features.
        layers (list): List of the number of nodes in each layer.
        L (int): Number of layers in the network.
        cache (dict): Dictionary to hold all intermediary values.
        weights (dict): Dictionary to hold all weights and biases.
    """

    def __init__(self, nx, layers):
        """Initializes the deep neural network.

        Args:
            nx (int): Number of input features.
            layers (list): List of the number of nodes in each layer.

        Raises:
            TypeError: If nx is not an integer or if layers is not a list
                of positive integers.
            ValueError: If nx is less than 1 or if layers is empty or
                contains non-positive integers.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be a positive integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")
        if any(not isinstance(x, int) or x < 1 for x in layers):
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for i in range(0, self.L):
            if layers[i] < 0 or not isinstance(layers[i], int):
                raise TypeError("layers must be a list of positive integers")
            self.weights['b{}'.format(i + 1)] = np.zeros(shape=(layers[i], 1))
            if i - 1 > - 1:
                he_et_al = np.sqrt(2 / layers[i - 1])
                Wn = np.random.randn(layers[i], layers[i - 1]) * he_et_al
                self.weights['W{}'.format(i + 1)] = Wn
            else:
                he_et_al = np.sqrt(2 / nx)
                Wn = np.random.randn(layers[i], nx) * he_et_al
                self.weights['W{}'.format(i + 1)] = Wn
