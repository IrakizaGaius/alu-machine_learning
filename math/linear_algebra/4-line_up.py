#!/usr/bin/env python3
"""
Module: 4-line_up
This module contains functions for matrix operations, including
matrix addition.
Functions:
    add_arrays(arr1, arr2): Returns the sum of two arrays."""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.
    Args:
        arr1: A list representing an array.
        arr2: A list representing an array.
    Returns:
        A new list representing the sum of the arrays.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
