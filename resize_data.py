# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:12:54 2021

@author: straw
"""
import os
import joblib
from skimage.io import imread
from skimage.transform import resize

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

data_path = r'C:\Users\straw\Desktop\AIS\ProjectPool 2\Classification-images\AnimalFace'
os.listdir(data_path)
print(os.listdir(data_path))
pklname = 'output'
width = 80
 
include = {'ChickenHead', 'BearHead', 'ElephantHead', 
           'EagleHead', 'DeerHead', 'MonkeyHead', 'PandaHead'}

resize_data(path=data_path, pklname=pklname, include=include, width=width)




