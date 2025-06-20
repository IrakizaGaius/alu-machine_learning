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

    loss = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits_v2(
            labels=y, logits=y_pred))
    return loss
