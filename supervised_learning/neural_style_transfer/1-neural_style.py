#!/usr/bin/env python3
"""Neural Style Transfer Class"""

import numpy as np
import tensorflow as tf

class NST:
    """Public Attributes"""
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                         'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'
    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        if not isinstance(style_image, np.ndarray) or len(style_image.shape) != 3:
            raise TypeError('style_image must be a numpy.ndarray with shape (h, w, 3)')

        if not isinstance(content_image, np.ndarray) or len(content_image.shape) != 3:
            raise TypeError('content_image must be a numpy.ndarray with shape (h, w, 3)')
        
        if alpha < 0:
            raise ValueError('alpha must be a non-negative number')

        if beta < 0:
            raise ValueError('beta must be a non-negative number')
        
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta
        self.model = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
        self.model.trainable = False

    def scale_image(self, image):
        """scales an image such that the pixels values are between 0 and 1
        and the largest side is 512 pixels"""
        if not isinstance(image, np.ndarray) or len(image.shape) != 3:
            raise TypeError('image must be a numpy.ndarray with shape (h, w, 3)')
        
        h, w, _ = image.shape
        if h > w:
            h_new = 512
            w_new = int(w * (512 / h))
        else:
            w_new = 512
            h_new = int(h * (512 / w))

        image = tf.image.resize(image, (h_new, w_new),
                                method='bicubic')
        image = image / 255.0
        image = tf.clip_by_value(image, 0.0, 1.0)
        # Add batch dimension
        image = tf.expand_dims(image, axis=0)
        return image
    
    def load_model(self):
        """creates the model used to calculate the cost"""
        style_outputs = [self.model.get_layer(name).output
                         for name in self.style_layers]
        content_output = self.model.get_layer(self.content_layer).output
        model_outputs = style_outputs + [content_output]

        return tf.keras.models.Model(self.model.input, model_outputs)
