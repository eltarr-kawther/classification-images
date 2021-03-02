# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:56:12 2021

@author: straw
"""
import os
from skimage.io import imread
from skimage.transform import resize
import joblib


def resize_data(path, pklname, include, width=150, height=None):
    """
    load images from path, resize them and write them as arrays to a dictionary,
    together with labels and metadata. The dictionary is written to a pickle file
    named '{pklname}_{width}x{height}px.pkl'.
    
    Parameter
    ---------
    src: str
        path to data
    pklname: str
        path to output file
    width: int
        target width of the image in pixels
    include: set[str]
        set containing str
    """
    height = height if height is not None else width
    data = dict()
    data['description'] = 'resized ({0}x{1})animal images in rgb'.format(int(width), int(height))
    data['label'] = []
    data['filename'] = []
    data['data'] = []
    
    pklname = f"Output/{pklname}_{width}x{height}px.pkl"
    for subdir in os.listdir(path):
        if subdir in include:
            current_path = os.path.join(path, subdir)
            for file in os.listdir(current_path):
                if file[-3:] in {'jpg', 'png'}:
                    im = imread(os.path.join(current_path, file), as_gray=False)
                    im = resize(im, (width, height))
                    data['label'].append(subdir[:-4])
                    data['filename'].append(file)
                    data['data'].append(im)
        joblib.dump(data, pklname)