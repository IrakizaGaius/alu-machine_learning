#!/usr/bin/env python3

"""Placeholders in TensorFlow"""

import tensorflow as tf


def create_placeholders(nx, classes):
    """
    Function that creates two placeholders in TensorFlow

    Args:
        nx (int): The number of feature columns
        classes (int): The number of classes in the classifier

    Returns:
        x: Placeholder for the input data
        y: Placeholder for the one-hot labels
    """
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.placeholder(tf.float32, shape=(None, classes), name='y')

    return x, y
