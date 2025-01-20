#!/usr/bin/env python3
"""
Module: 3-flip_me_over
This module contains functions for matrix operations, including
matrix transpose.
Functions:
    matrix_transpose(matrix): Returns the transpose of the matrix."""


def matrix_transpose(matrix):
    """
    Transposes a matrix.
    Args:
        matrix: A list (or nested lists) representing a matrix.
    Returns:
        A new transposed matrix.
    """
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]
