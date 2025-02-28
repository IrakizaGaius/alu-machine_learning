
# Multivariate Probability Project

## 🎯 Learning Objectives

- Understand joint/multivariate distributions
- Calculate covariance matrices and correlation coefficients
- Implement multivariate Gaussian distributions
- Explain Carl Friedrich Gauss' contributions
- Work with variance-covariance matrices

## 📂 Project Structure

multivariate_prob/
├── 0-mean_cov.py        # Mean & covariance calculator
├── 1-correlation.py     # Correlation matrix generator
├── multinormal.py       # Multivariate Normal distribution class
└── README.md            # Project documentation

Copy

## ⚙️ Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install numpy==1.15
```

🚀 Usage Examples
Task 0: Mean and Covariance

```python

import numpy as np
from 0-mean_cov import mean_cov

X = np.random.multivariate_normal([12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000)
mean, cov = mean_cov(X)
```

# Output: [[12.04 29.93 10.01]] and 3x3 covariance matrix

```python
Task 1: Correlation Matrix
from 1-correlation import correlation
C = np.array([[36, -30, 15], [-30, 100, -20], [15, -20, 25]])
print(correlation(C))
```

# Output: 3x3 correlation matrix with values between -1 and 1

Task 2/3: Multivariate Normal Distribution

```python
from multinormal import MultiNormal

data = np.random.multivariate_normal([12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000).T
mn = MultiNormal(data)
x = np.array([[8.2], [32.8], [9.67]])
print(f"PDF value: {mn.pdf(x):.6f}")  # Output: ~0.000229
```

🔧 Technical Requirements
Python 3.5 & numpy 1.15
Strict pycodestyle compliance (v2.5)
Complete documentation for all functions/classes
100% numpy implementation (no external libs)
Executable files with shebang #!/usr/bin/env python3
📖 Key Resources
Core Concepts

Joint Probability Distributions
Multivariate Gaussian Properties
Covariance-Correlation Relationships
Numerical Methods

Matrix Inversion/Determinant Calculations
Efficient Multivariate Sampling
Numerical Stability Techniques
References

numpy.cov/numpy.corrcoef documentation
Factor Analysis Matrix Notation
Gauss' Original Distribution Papers
