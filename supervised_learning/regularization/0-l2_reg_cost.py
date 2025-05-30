#!/usr/bin/env python3
"""Cost of a neural network using L2 Regularization"""

import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """Function to calculate the cost of a model using L2 regularization"""
    reg_cost = 0
    for i in range(1, L + 1):
        reg_cost += np.linalg.norm(weights['W' + str(i)]) ** 2
    reg_cost *= lambtha / (2 * m)
    return cost + reg_cost
