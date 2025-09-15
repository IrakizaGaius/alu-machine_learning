#!/usr/bin/env python3

"""
    Function that performs forward propagation for a simple RNN
    rnn(rnn_cell, X, h_0)
        rnn_cell: instance of RNNCell
        X: input data for the RNN
        h_0: initial hidden state
    Returns:
        h: hidden states for all time steps
        y: outputs for all time steps
"""
import numpy as np

def rnn(rnn_cell, X, h_0):
    """
    Function that performs forward propagation for a simple RNN

    Parameters:
        rnn_cell [instance of RNNCell]: the cell to use for the RNN
        X [np.ndarray of shape (t, m, i)]: contains the data input
            t: number of time steps
            m: batch size for the data
            i: dimensionality of the data
        h_0 [np.ndarray of shape (m, h)]: contains the initial hidden state
            m: batch size for the data
            h: dimensionality of the hidden state
    Returns:
        h [np.ndarray of shape (t, m, h)]: contains all the hidden states
            t: number of time steps
            m: batch size for the data
            h: dimensionality of the hidden state
        y [np.ndarray of shape (t, m, o)]: contains all the outputs
            t: number of time steps
            m: batch size for the data
            o: dimensionality of the outputs
    """
    t, m, i = X.shape
    h = np.zeros((t, m, rnn_cell.Wh.shape[1]))
    y = np.zeros((t, m, rnn_cell.Wy.shape[1]))

    h_next = h_0
    for step in range(t):
        h_next, y_next = rnn_cell.forward(h_next, X[step])
        h[step] = h_next
        y[step] = y_next

    return h, y