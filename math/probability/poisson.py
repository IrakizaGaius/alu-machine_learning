#!/usr/bin/env python3
"""
Poisson distribution
"""


class Poisson:
    """
    Class Poisson that represents a poisson distribution
    """
    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor
        """
        if data is None:
            self.lambtha = float(lambtha)
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        elif type(data) is not list:
            raise TypeError("data must be a list")
        elif len(data) < 2:
            raise ValueError("data must contain multiple values")
        else:
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """
        Probability Mass Function
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        return ((2.7182818285 ** (-self.lambtha)) *
                (self.lambtha ** k)) / factorial
