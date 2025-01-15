#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


y = np.arange(0, 11) ** 3
# Plotting the graph
plt.plot(range(0, 11), y, 'r-', label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Graph of y = x^3')
plt.legend()
plt.show()
