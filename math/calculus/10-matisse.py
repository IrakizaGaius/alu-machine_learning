#!/usr/bin/env python3
"""Derivative of a polynomial"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial"""
    # Validate input
    if not isinstance(poly, list):
        return None
    if any(not isinstance(x, (int, float)) for x in poly):
        return None
    if len(poly) == 0:  # Ensure an empty polynomial returns None
        return None
    if len(poly) == 1:  # The derivative of a constant is 0
        return [0]
    # Compute the derivative
    derivative = [poly[i] * i for i in range(1, len(poly))]
    # Trim trailing zeros to match expected format
    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()
    return derivative
