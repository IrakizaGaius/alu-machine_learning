#!/usr/bin/env python3
"""Create a layer in TensorFlow"""

import tensorflow as tf


def create_layer(prev, n, activation):
    """
    Function that creates a layer in TensorFlow

    Args:
        prev (tensor): The output of the previous layer
        n (int): The number of nodes in the layer to create
        activation (function): The activation function to use on the layer

    Returns:
        tensor: The output of the layer
    """
    return tf.layers.Dense(units=n, activation=activation)(prev)
