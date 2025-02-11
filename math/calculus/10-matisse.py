#!/usr/bin/env python3
"""Derivative of a polynomial"""


def poly_derivative(poly: list) -> list:
    """Derivative of a polynomial"""
    if not isinstance(poly, list) or any(not isinstance(i, (int, float)) for i in poly):
        return None
    if len(poly) <= 1:
        return None  # Return None for an empty or single-element list
    return [
        poly[i] * i for i in range(1, len(poly))
    ]
