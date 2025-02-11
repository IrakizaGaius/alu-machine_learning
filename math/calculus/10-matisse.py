#!/usr/bin/env python3
"""Derivative of a polynomial"""


def poly_derivative(poly: list) -> list:
    """Derivative of a polynomial"""
    if not isinstance(poly, list) or not all(isinstance(i, (int, float)) for i in poly):
        return None
    return [poly[i] * i for i in range(1, len(poly))] if len(poly) > 1 else [0]
