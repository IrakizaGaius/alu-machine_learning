#!/usr/bin/env python3

import numpy as np

class RNNCell:
    """
    Class that represents a cell of a simple RNN

    Public instance attributes:
        Wh: the weight matrix for the hidden state
        Wy: the weight matrix for the output
        bh: the bias for the hidden state
        by: the bias for the output

    Class constructor:
        def __init__(self, i, h, o)
            i: dimensionality of the data
            h: dimensionality of the hidden state
            o: dimensionality of the outputs
    """

    def __init__(self, i, h, o):
        """
        Class constructor for RNNCell

        Parameters:
            i [int]: dimensionality of the data
            h [int]: dimensionality of the hidden state
            o [int]: dimensionality of the outputs
        """
        self.Wh = np.random.randn(h + i, h)
        self.Wy = np.random.randn(h, o)
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Public instance method that performs forward propagation for one time step

        Parameters:
            h_prev [np.ndarray of shape (m, h)]: contains the previous hidden state
                m: batch size for the data
                h: dimensionality of the hidden state
            x_t [np.ndarray of shape (m, i)]: contains the data input for the cell
                m: batch size for the data
                i: dimensionality of the data
        Returns:
            h_next [np.ndarray of shape (m, h)]: next hidden state
            y [np.ndarray of shape (m, o)]: output of the cell
                o: dimensionality of the outputs
        """
        # Concatenate h_prev and x_t along the last axis
        concat = np.concatenate((h_prev, x_t), axis=1)

        # Compute the next hidden state
        h_next = np.tanh(np.matmul(concat, self.Wh) + self.bh)

        # Compute the output
        y = np.matmul(h_next, self.Wy) + self.by

        return h_next, y
