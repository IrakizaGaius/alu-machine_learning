# Calculus Project

## Project Overview

This project is focused on fundamental concepts in calculus, including summation and product notation, series, derivatives, integration, and partial derivatives. The project consists of multiple-choice questions and Python scripts that implement calculus-related computations.

## How the Answers Are Determined

### Multiple-Choice Questions

For the multiple-choice questions, the correct answers are derived using fundamental calculus principles:

- **Summation Notation**: The sum of a sequence of numbers is computed using the sigma notation.
- **Product Notation**: The product of a sequence of numbers is determined using pi notation.
- **Derivatives**: Differentiation is performed using basic rules such as the power rule, product rule, and chain rule.
- **Partial Derivatives**: Partial differentiation is applied to multivariable functions.
- **Integrals**: The indefinite and definite integrals are computed using standard integral rules.

Each answer file should contain only the number corresponding to the correct choice, ensuring correctness according to the problem statement.

### Python Scripts

The Python scripts are used to calculate summations, derivatives, and integrals programmatically. The following rules are applied:

#### 1. Summation of Squares (`9-sum_total.py`)

- Uses the formula for the sum of squares:
  \[ \sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} \]
- Implemented without loops, using direct mathematical computation.

#### 2. Polynomial Derivatives (`10-matisse.py`)

- Given a list representing a polynomial, the derivative is calculated using the power rule:
  \[ \frac{d}{dx} (ax^n) = n \cdot ax^{n-1} \]
- If the input is invalid, the function returns `None`.

#### 3. Polynomial Integrals (`17-integrate.py`)

- Computes the indefinite integral of a polynomial:
  \[ \int ax^n dx = \frac{a}{n+1} x^{n+1} + C \]
- Returns a list representing the integral’s coefficients.

## Requirements

- All Python scripts must be executable (`chmod +x filename.py`).

- The first line of every script should be `#!/usr/bin/env python3`.
- Code must follow `pycodestyle` (PEP 8) guidelines.
- Functions, classes, and modules must include documentation.
- No external libraries are allowed.

## Repository Structure

```plaintext
alu-machine_learning/
│── math/
│   ├── calculus/
│   │   ├── 0-sigma_is_for_sum
│   │   ├── 1-seegma
│   │   ├── 2-pi_is_for_product
│   │   ├── ...
│   │   ├── 9-sum_total.py
│   │   ├── 10-matisse.py
│   │   ├── 17-integrate.py
│   │   ├── README.md
```
