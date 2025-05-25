#!/usr/bin/env python3

"""Module which contains calculate_loss"""
import tensorflow as tf


def calculate_loss(y, y_pred):
    """
    Calculates the softmax cross-entropy loss of a prediction

    Args:
        y (tf.placeholder): placeholder for the one-hot labels
        y_pred (tf.Tensor): tensor containing the predicted labels

    Returns:
        tf.Tensor: tensor containing the loss of the prediction
    """

    return tf.compat.v1.losses.softmax_cross_entropy(y, y_pred)
