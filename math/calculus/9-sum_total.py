#!/usr/bin/env python3
"""Sum of the squares of the first n natural numbers"""


def summation_i_squared(n: int) -> int:
    """Sum of the squares of the first n natural numbers"""
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
