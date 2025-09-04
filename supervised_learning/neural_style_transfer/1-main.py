#!/usr/bin/env python3

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

NST = __import__('1-neural_style').NST


if __name__ == '__main__':
    style_image = mpimg.imread("supervised_learning/neural_style_transfer/starry_night.jpg")
    content_image = mpimg.imread("supervised_learning/neural_style_transfer/golden_gate.jpg")

    nst = NST(style_image, content_image)
    nst.model.summary()
