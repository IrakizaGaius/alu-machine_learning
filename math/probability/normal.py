#!/usr/bin/env python3
"""Normal distribution"""


class Normal:
    """Normal distribution class"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Constructor"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        elif type(data) is not list:
            raise TypeError("data must be a list")
        else:
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            sum_squared_diffs = sum((x - self.mean) ** 2 for x in data)
            variance = sum_squared_diffs / len(data)
            self.stddev = variance ** 0.5

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""
        exponent = -1 * ((x - self.mean) ** 2 / (2 * (self.stddev ** 2)))
        numerator = 2.7182818285 ** exponent
        denominator = self.stddev * (2 * 3.1415926536) ** 0.5
        return numerator / denominator

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value"""
        scaled_x = (x - self.mean) / (self.stddev * (2 ** 0.5))
        erf_approx = (2 / (3.1415926536 ** 0.5)) * (
            scaled_x - (scaled_x ** 3) / 3 + (scaled_x ** 5) / 10
            - (scaled_x ** 7) / 42 + (scaled_x ** 9) / 216)
        return (1 + erf_approx) / 2
