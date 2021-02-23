# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 21:02:04 2021

@author: straw
"""
from sklearn.base import BaseEstimator, TransformerMixin
import skimage
import numpy as np

class RGB2GrayTransformer(BaseEstimator, TransformerMixin):
    """
    Convert an array of RGB images to grayscale
    """
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        T = np.array([skimage.color.rgb2gray(img) for img in X])
        return T
