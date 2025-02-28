# Bayesian Probability Project

## Project Overview

This repository implements Bayesian probability calculations for clinical trial analysis, focusing on calculating likelihoods, intersections, marginal probabilities, and posterior distributions. Designed for Python 3.5 with NumPy 1.15, it follows strict coding standards and documentation requirements.

## Resources

- **Core Concepts**:
  - [Bayesian Probability](https://en.wikipedia.org/wiki/Bayesian_probability)
  - [Bayes' Theorem Explained](https://www.youtube.com/watch?v=HZGCoVF3YvM)
  - [Base Rate Fallacy](https://towardsdatascience.com/base-rate-fallacy-3893e16e59db)
- **Video Courses**:
  - [Bayesian Statistics Course](https://www.coursera.org/specializations/bayesian-statistics)
- **Mathematical Guides**:
  - [Bayesian Inference Visualization](https://seeing-theory.brown.edu/bayesian-inference/index.html)

## Learning Objectives

- Understand Bayesian vs Frequentist probability
- Implement Bayes' rule for statistical inference
- Calculate:
  - Prior/posterior distributions
  - Likelihood functions
  - Marginal probabilities
  - Bayesian intersections

## Requirements

```bash
Python 3.5 | NumPy 1.15 | Ubuntu 16.04 LTS
* Code Quality:
    * PEP8 compliance (pycodestyle 2.5)
    * Full module/class/function documentation
    * Executable files with shebang #!/usr/bin/env python3
Installation
bash

Copy
git clone https://github.com/alu-machine_learning/math/bayesian_prob.git
cd bayesian_prob
python3 -m venv bayes_env
source bayes_env/bin/activate
pip install numpy==1.15
```

Project Structure
File    Description    Key Features
0-likelihood.py Calculates binomial likelihoods - Input validation

- Vectorized operations

1-intersection.py  Computes probability intersections - Prior distribution checks

- NumPy array validation
2-marginal.py Calculates marginal probabilities - Error chaining

- Precision handling
3-posterior.py Computes posterior distributions - Bayesian updating
- Numerical stability

Usage Examples

1. Likelihood Calculation

```python

import numpy as np
from '0-likelihood' import likelihood

P = np.linspace(0, 1, 11)
print(likelihood(26, 130, P))
# Output: [0.00e+00 2.71e-04 8.72e-02 ... 0.00e+00]
2. Posterior Distribution Analysis
python

Copy
from '3-posterior' import posterior

P = np.linspace(0, 1, 11)
Pr = np.ones(11)/11
print(posterior(26, 130, P, Pr))
# Output: [0.00e+00 2.99e-03 9.63e-01 ... 0.00e+00]
```

Key Algorithms

- Binomial Likelihood:mathCopy\mathcal{L}(p) = C(n,x) \cdot p^x \cdot (1-p)^{n-x}

- Bayesian Update:mathCopyP(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}

Validation Framework
All functions include comprehensive error checking:

```python

Copy
# Example validation sequence from 1-intersection.py
if not isinstance(P, np.ndarray) or P.ndim != 1:
    raise TypeError("P must be a 1D numpy.ndarray")
if not np.all((P >= 0) & (P <= 1)):
    raise ValueError("All values in P must be in [0, 1]")
```
