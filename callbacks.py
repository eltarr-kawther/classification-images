# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:05:50 2021

@author: straw
"""
import os
from dash.dependencies import Input, Output, State
from app import app
from layouts import parse_contents, save_file
import joblib
from skimage.io import imread
from skimage.transform import resize


@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'))
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None and list_of_names is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
        return children

@app.callback(Output('output-prediction', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'))
def update_prediction(list_of_contents, list_of_names):
    directory = 'Output\Mimoun'
    if list_of_contents is not None and list_of_names is not None:
        for content, name in zip(list_of_contents, list_of_names):
            files_in_dir = os.listdir(directory)
            exts = {".jpg", ".png", ".gif"}
            filtered_files = [file for file in files_in_dir if any(file.endswith(s) for s in exts)]
            for img in filtered_files:
                if len(filtered_files) >=1:
                    path_to_file = os.path.join(directory,img)
                    os.remove(path_to_file)
            save_file(name, content)
    
    #best_estimator = joblib.load('Output/models/best_model.pkl')
    model = joblib.load('Output/models/hog_models.pkl')
    width = 80
    height = 80
    images = []
    for file in os.listdir(directory):
        file = imread(os.path.join(directory, file), as_gray=False)
        file = resize(file, (width, height))
        #file_gray = best_estimator['grayify'].transform(file)
        #file_hog = best_estimator['hogify'].transform(file_gray)
        #file_prepared = best_estimator['scalify'].transform(file_hog)
        images.append(file)
    images.append(images[0])           
    prediction = model.predict(images)
    return prediction[0]
        
    
