#!/usr/bin/env python3
""""
Module: 5-across_the_planes
This module contains functions for matrix operations, including
matrix addition.
Functions:
    add_matrices2D(mat1, mat2): Returns the sum of two 2D matrices. """


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.
    Args:
        mat1: A list (or nested lists) representing a 2D matrix.
        mat2: A list (or nested lists) representing a 2D matrix.
    Returns:
        A new list representing the sum of the matrices.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
            for i in range(len(mat1))]
