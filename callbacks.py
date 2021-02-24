# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:05:50 2021

@author: straw
"""
import os
from dash.dependencies import Input, Output, State
from app import app
from layouts import save_file
import joblib

@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None and list_of_names is not None :
        for content, name in zip(list_of_contents, list_of_names):
            directory = './Output/temp'
            files_in_dir = os.listdir(directory)
            exts = {".jpg", ".png", ".gif"}
            filtered_files = [file for file in files_in_dir if any(file.endswith(s) for s in exts)]
            for img in filtered_files:
                if len(filtered_files) >=1:
                    path_to_file = os.path.join(directory,img)
                    os.remove(path_to_file)
            save_file(name, content)
    #model = joblib.load()
