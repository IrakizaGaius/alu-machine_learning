# Convolutions and Pooling Project

## 🧠 Learning Objectives

Understand and implement:

- Convolution operations (valid/same/padded/strided)
- Multi-channel & multi-kernel convolutions
- Pooling operations (max/average)
- Key CNN concepts:
  - Kernels/filters
  - Padding strategies
  - Stride mechanics
  - Channel management

---

## 🛠️ Project Tasks

### 0. Valid Convolution [`0-convolve_grayscale_valid.py`]

Implement valid convolution for grayscale images (no padding).  
**Input**: (50000, 28, 28)  
**Output**: (50000, 26, 26)  

### 1. Same Convolution [`1-convolve_grayscale_same.py`]

Maintain input dimensions through zero-padding.  
**I/O Consistency**: (50000, 28, 28) → (50000, 28, 28)

### 2. Custom Padding Convolution [`2-convolve_grayscale_padding.py`]

Flexible padding configuration with tuple input.  
**Example**: (2,4) padding → 28×28 → 30×34

### 3. Strided Convolution [`3-convolve_grayscale.py`]

Implement strided operations with padding options.  
**Stride Demo**: (2,2) stride reduces 28×28 → 13×13

### 4. Multi-Channel Convolution [`4-convolve_channels.py`]

Process RGB images with channel-wise kernels.  
**Animal Dataset**: 32×32×3 → 30×30

### 5. Multi-Kernel Convolution [`5-convolve.py`]

Apply multiple filters simultaneously.  
**Output Channels**: 3 kernels → 3 output channels

### 6. Pooling Operations [`6-pool.py`]

Implement max/average pooling with configurable window.  
**Pooling Demo**: 32×32 → 16×16 with 2×2 window

---

## ⚙️ Technical Requirements

- **Python 3.5** with **NumPy 1.15**

- Strict pycodestyle (v2.5) compliance
- Complete documentation for all modules/functions
- Limited to:
  - 2-3 nested loops maximum
  - NumPy and basic math imports
  - No `np.convolve` usage

---

## 🗄️ Repository Structure

alu-machine_learning/
└── math/
└── convolutions_and_pooling/
├── 0-convolve_grayscale_valid.py
├── 1-convolve_grayscale_same.py
├── 2-convolve_grayscale_padding.py
├── 3-convolve_grayscale.py
├── 4-convolve_channels.py
├── 5-convolve.py
├── 6-pool.py
└── README.md
