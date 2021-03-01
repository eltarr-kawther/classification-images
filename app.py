# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:04:48 2021

@author: straw
"""
import dash
from transformers import RGB2GrayTransformer, HogTransformer

BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/minty/bootstrap.min.css"

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[BS])
server = app.server
app.title = "Arche de Noé"
