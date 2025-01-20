#!/usr/bin/env python3
"""
Module: 2-size_me_please
This module contains functions for matrix operations, including
calculating the shape (dimensions) of a matrix.
Functions:
    matrix_shape(matrix): Returns the shape of the matrix, represented
    as a list of integers indicating the number of rows, columns, etc.
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix.
    Args:
        matrix: A list (or nested lists) representing a matrix.
    Returns:
        A list of integers representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
