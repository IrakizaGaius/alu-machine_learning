#!/usr/bin/env python3

"""Same Convolution on Grayscale Images"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """performs a same convolution on grayscale images"""
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph = kh // 2
    pw = kw // 2
    images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')
    output_h = h
    output_w = w
    output = np.zeros((m, output_h, output_w))
    for i in range(output_h):
        for j in range(output_w):
            output[:, i, j] = np.sum(
                images[:, i: i + kh, j: j + kw] * kernel, axis=(1, 2)
            )
    return output
