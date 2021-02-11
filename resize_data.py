# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:12:54 2021

@author: straw
"""
import os
import joblib
from collections import Counter

from skimage.io import imread
from skimage.transform import resize

import numpy as np

import matplotlib.pyplot as plt

#os.chdir(r'C:\Users\straw\Desktop\AIS\ProjectPool 2\Classification-images')

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
            print(subdir)
            current_path = os.path.join(path, subdir)
            
            for file in os.listdir(current_path):
                if file[-3:] in {'jpg', 'png'}:
                    im = imread(os.path.join(current_path, file))
                    im = resize(im, (width, height)) #[:,:,::-1]
                    data['label'].append(subdir[:-4])
                    data['filename'].append(file)
                    data['data'].append(im)
        joblib.dump(data, pklname)
    return data

data_path = r'C:\Users\straw\Desktop\AIS\ProjectPool 2\Classification-images\AnimalFace'
os.listdir(data_path)
print(os.listdir(data_path))
pklname = 'output'
width = 80
 
include = {'ChickenHead', 'BearHead', 'ElephantHead', 
           'EagleHead', 'DeerHead', 'MonkeyHead', 'PandaHead'}

resize_data(path=data_path, pklname=pklname, include=include, width=width)


data = joblib.load(f'Output/{pklname}_{width}x{width}px.pkl')
 
print('number of samples: ', len(data['data']))
print('keys: ', list(data.keys()))
print('description: ', data['description'])
print('image shape: ', data['data'][0].shape)
print('labels:', np.unique(data['label']))
 
Counter(data['label'])

# use np.unique to get all unique values in the list of labels
labels = np.unique(data['label'])
 
# set up the matplotlib figure and axes, based on the number of labels
fig, axes = plt.subplots(1, len(labels))
fig.set_size_inches(15,4)
fig.tight_layout()
 
# make a plot for every label (equipment) type. The index method returns the 
# index of the first item corresponding to its search string, label in this case
for ax, label in zip(axes, labels):
    idx = data['label'].index(label)
     
    ax.imshow(data['data'][idx])
    ax.axis('off')
    ax.set_title(label)

X = np.array(data['data'])
y = np.array(data['label'])

