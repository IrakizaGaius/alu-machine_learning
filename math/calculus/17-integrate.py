#!/usr/bin/env python3
"""Integral of a polynomial"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial"""

    # Validate input
    if not isinstance(poly, list) or not isinstance(C, (int, float)):
        return None
    if len(poly) == 0 or any(not isinstance(x, (int, float)) for x in poly):
        return None
    # Compute the integral
    integral = [C]  # Add constant of integration first
    for i in range(len(poly)):
        new_coef = poly[i] / (i + 1)
        # Convert whole numbers to int, keep decimals as floats
        if new_coef.is_integer():
            new_coef = int(new_coef)
        integral.append(new_coef)
    # Trim trailing zeros
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
