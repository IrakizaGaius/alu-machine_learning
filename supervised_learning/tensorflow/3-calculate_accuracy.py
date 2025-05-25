#!/usr/bin/env python3

"""
module which contains calculate_accuracy"""

import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    calculates the accuracy of a prediction

    Args:
        y (tf.placeholder): placeholder for the one-hot labels
        y_pred (tf.Tensor): tensor containing the predicted labels

    Returns:
        tf.Tensor: tensor containing the accuracy of the prediction
    """
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    return accuracy
