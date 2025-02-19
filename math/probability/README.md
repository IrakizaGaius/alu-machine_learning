# Probability Distributions Project

## 🎯 Learning Objectives

### General Concepts

- Define probability and its notation  
- Understand independence vs. disjoint events  
- Apply addition/multiplication rules for unions/intersections  
- Explain probability distributions (PMF/PDF/CDF)  
- Calculate mean, variance, standard deviation, and percentiles  

### Key Distributions

1. **Poisson**  
2. **Exponential**  
3. **Normal**  
   - Empirical Rule  
   - Z-score calculations  
4. **Binomial**  

---

## ⚙️ Requirements

### General

- **Environment**: Ubuntu 16.04 LTS, Python 3.5
- **Style**: `pycodestyle` (v2.5) compliant  
- **Documentation**:  
  - Module/class/function docstrings required  
  - Execute `python3 -c 'print(__import__("my_module").__doc__)'` for verification  
- **Execution**:  
  - All files must be executable  
  - No external imports allowed unless specified  

### Mathematical Approximations

- **π**: `3.1415926536`  
- **e**: `2.7182818285`  

---

## 📂 Tasks & Files

### Poisson Distribution (`poisson.py`)

- **Task 0**: Initialize `Poisson` class with `data` or `lambtha`  
- **Task 1**: Implement PMF calculation (`pmf(k)`)  
- **Task 2**: Implement CDF calculation (`cdf(k)`)  

### Exponential Distribution (`exponential.py`)

- **Task 3**: Initialize `Exponential` class  
- **Task 4**: Calculate PDF (`pdf(x)`)  
- **Task 5**: Calculate CDF (`cdf(x)`)  

### Normal Distribution (`normal.py`)

- **Task 6**: Initialize `Normal` class with `data` or `mean/stddev`  
- **Task 7**: Compute z-scores (`z_score(x)`) and x-values (`x_value(z)`)  
- **Task 8**: Calculate PDF (`pdf(x)`)  
- **Task 9**: Calculate CDF (`cdf(x)`)  

### Binomial Distribution (`binomial.py`)

- **Task 10**: Initialize `Binomial` class with `data` or `n/p`  
- **Task 11**: Implement PMF (`pmf(k)`)  
- **Task 12**: Implement CDF (`cdf(k)`)  

---

## 🛠 Usage Example

```python
# Poisson Example
import numpy as np
from poisson import Poisson

np.random.seed(0)
data = np.random.poisson(5., 100).tolist()
p = Poisson(data)
print("PMF(9):", p.pmf(9))  # Output: ~0.0318
print("CDF(9):", p.cdf(9))  # Output: ~0.9736
