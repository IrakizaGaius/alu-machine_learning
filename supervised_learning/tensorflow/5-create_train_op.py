#!/usr/bin/env python3

"""Train operation for a neural network in TensorFlow."""
import tensorflow as tf


def create_train_op(loss, alpha):
    """
    Creates a training operation using Adam optimization.

    Args:
        loss (tf.Tensor): The loss tensor to minimize.
        alpha (float): The learning rate.

    Returns:
        tf.Operation: The training operation.
    """
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    train_op = optimizer.minimize(loss)
    return train_op
