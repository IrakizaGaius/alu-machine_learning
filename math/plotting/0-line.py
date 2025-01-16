#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x0 = 0
xf = 10

x = np.arange(x0, xf + 1)
y = x ** 3

plt.plot(x, y, 'r-', label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Graph of y = x^3')
plt.xlim([x.min(), x.max()])
plt.ylim([y.min(), y.max()])
plt.legend()
plt.show()
