# Neural Style Transfer

This project implements Neural Style Transfer (NST) using TensorFlow, a deep learning technique that combines the content of one image with the artistic style of another image.

## Overview

Neural Style Transfer is an optimization technique used to take two images—a content image and a style reference image (such as an artwork by a famous painter)—and blend them together so the output image looks like the content image, but "painted" in the style of the style reference image.

## Project Structure

```
neural_style_transfer/
├── 0-neural_style.py     # Basic NST class implementation
├── 1-neural_style.py     # Load model functionality
├── 2-neural_style.py     # Gram matrix calculation
├── 3-neural_style.py     # Extract features
├── 4-neural_style.py     # Layer style cost
├── 5-neural_style.py     # Style cost calculation
├── 6-neural_style.py     # Content cost calculation
├── 7-neural_style.py     # Total cost calculation
├── 8-neural_style.py     # Compute gradients
├── 9-neural_style.py     # Generate image
├── 10-neural_style.py    # Variational cost
├── *-main.py             # Test files for each implementation
├── starry_night.jpg      # Style reference image
├── golden_gate.jpg       # Content image
└── README.md             # This file
```

## Requirements

- Python 3.x
- TensorFlow 2.x
- NumPy
- Matplotlib (for visualization)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd alu-machine_learning/supervised_learning/neural_style_transfer
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

3. Install required packages:
```bash
pip install tensorflow numpy matplotlib
```

## Usage

### Basic Usage

```python
import matplotlib.image as mpimg
from neural_style_transfer import NST

# Load images
style_image = mpimg.imread("starry_night.jpg")
content_image = mpimg.imread("golden_gate.jpg")

# Create NST instance
nst = NST(style_image, content_image, alpha=1e4, beta=1)

# The images are automatically scaled and preprocessed
print(f"Style image shape: {nst.style_image.shape}")
print(f"Content image shape: {nst.content_image.shape}")
```

### Running Tests

Each module comes with its own test file. Run them individually:

```bash
python 0-main.py  # Test basic NST class
python 1-main.py  # Test model loading
python 2-main.py  # Test Gram matrix
# ... and so on
```

## Class Documentation

### NST Class

The main Neural Style Transfer class with the following components:

#### Class Attributes
- `style_layers`: List of VGG19 layers used for style extraction
- `content_layer`: VGG19 layer used for content extraction

#### Constructor Parameters
- `style_image`: numpy array of shape (h, w, 3) containing the style image
- `content_image`: numpy array of shape (h, w, 3) containing the content image
- `alpha`: Weight for content cost (default: 1e4)
- `beta`: Weight for style cost (default: 1)

#### Methods

##### `scale_image(image)`
Scales an image such that:
- Pixel values are between 0 and 1
- The largest side is 512 pixels
- Maintains aspect ratio
- Adds batch dimension for neural network processing

**Parameters:**
- `image`: numpy array of shape (h, w, 3)

**Returns:**
- TensorFlow tensor of shape (1, h_new, w_new, 3)

## Key Concepts

### Style Layers
The style is extracted from multiple layers of the VGG19 network:
- `block1_conv1`: Low-level features (edges, textures)
- `block2_conv1`: Mid-level features
- `block3_conv1`: Higher-level patterns
- `block4_conv1`: Complex patterns
- `block5_conv1`: High-level abstract features

### Content Layer
Content is typically extracted from deeper layers:
- `block5_conv2`: High-level content representation

### Loss Function
The total loss combines:
- **Content Loss**: Measures how much the generated image differs from the content image
- **Style Loss**: Measures how much the generated image differs from the style image
- **Total Variation Loss**: Encourages spatial smoothness (optional)

## Images

The project includes sample images:
- `starry_night.jpg`: Famous Van Gogh painting used as style reference
- `golden_gate.jpg`: Content image of the Golden Gate Bridge

## Algorithm Flow

1. **Preprocessing**: Scale and normalize input images
2. **Feature Extraction**: Use VGG19 to extract features from multiple layers
3. **Style Representation**: Compute Gram matrices for style layers
4. **Content Representation**: Extract content features
5. **Optimization**: Minimize combined loss function
6. **Post-processing**: Convert result back to displayable image

## Technical Details

### VGG19 Architecture
The project uses the VGG19 convolutional neural network, pre-trained on ImageNet, as the feature extractor. VGG19 is chosen because:
- It has been proven effective for style transfer
- Pre-trained weights capture useful feature representations
- Layer hierarchy allows multi-scale style extraction

### Gram Matrix
Style is represented using Gram matrices, which capture:
- Correlations between different feature maps
- Style information independent of spatial layout
- Statistical properties of textures and patterns

## Performance Considerations

- Image size affects processing time (larger images take longer)
- Number of optimization iterations impacts quality and time
- GPU acceleration recommended for faster processing
- Memory usage scales with image size and batch size

## Troubleshooting

### Common Issues

1. **Memory Errors**: Reduce image size or use smaller batch sizes
2. **Import Errors**: Ensure TensorFlow is properly installed
3. **Shape Mismatches**: Verify input images have 3 channels (RGB)
4. **Slow Performance**: Use GPU acceleration if available

### Error Messages

- `TypeError: style_image must be a numpy.ndarray with shape (h, w, 3)`: Input must be RGB image
- `ValueError: alpha must be a non-negative number`: Check parameter values
- `ValueError: beta must be a non-negative number`: Check parameter values

## Examples

See the `*-main.py` files for complete examples of how to use each component of the neural style transfer implementation.

## References

- Gatys, Leon A., Alexander S. Ecker, and Matthias Bethge. "A neural algorithm of artistic style." arXiv preprint arXiv:1508.06576 (2015).
- Johnson, Justin, Alexandre Alahi, and Li Fei-Fei. "Perceptual losses for real-time style transfer and super-resolution." European conference on computer vision. Springer, 2016.

## License

This project is part of the ALU Machine Learning curriculum.

## Contributing

Please follow the project guidelines and ensure all tests pass before submitting contributions.
