# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:05:50 2021

@author: straw
"""
from dash.dependencies import Input, Output
from app import app

@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
