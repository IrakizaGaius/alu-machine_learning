#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Plotting the histogram
plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')
plt.xticks(range(0, 101, 10))
plt.yticks(range(0, 31, 5))
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.show()
