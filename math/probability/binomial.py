#!/usr/bin/env python3
"""
Binomial distribution
"""


class Binomial:
    """
    Class Binomial
    """
    def __init__(self, data=None, n=1, p=0.5):
        """
        Class constructor
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = n
            self.p = p
        elif type(data) is not list:
            raise TypeError("data must be a list")
        else:
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum([(x - mean) ** 2 for x in data]) / len(data)
            p = 1 - variance / mean
            n = round(mean / p)
            p = mean / n
            self.n = n
            self.p = p

    def comb(self, n, k):
        """
        Calculates the factorial of a number
        """
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        k = min(k, n - k)
        result = 1
        for i in range(k):
            result *= (n - i)
            result //= (i + 1)
        return result

    def pmf(self, k):
        """
        PMF for a given number of successes
        """
        if k < 0 or k > self.n:
            return 0
        k = int(k)
        p = self.p
        binomial_coefficient = self.comb(self.n, k)
        return binomial_coefficient * (p ** k) * ((1 - p) ** (self.n - k))

    def cdf(self, k):
        """
        CDF for a given number of successes
        """
        if k < 0:
            return 0
        k = int(k)
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
