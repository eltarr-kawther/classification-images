# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:07:33 2021

@author: straw
"""
import os
import base64
import datetime
import io
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table

import pandas as pd


layout1 = html.Div(children=[
    html.Div(className="welcome-page-title", children=[html.P('Bienvenue sur l\'Arche de Noé')]),
    html.Br(),
    dbc.Button(dcc.Link('Embarquer', href='/app2'), color="warning", className="btn btn-primary")
    ], style={
  'verticalAlign':'middle',
  'textAlign': 'center',
  'background-image': 'url("/assets/noah.jpg")',
  'position':'fixed',
  'width':'100%',
  'height':'100%',
  'top':'0px',
  'left':'0px',
  'z-index':'1000'
})

layout2 = html.Div([
    dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Accueil", href="/")),
        dbc.NavItem(dbc.NavLink("Catalogue d'images", href="#")),
    ],
    brand="L'Arche de Noé",
    brand_href="/",
    color="primary",
    dark=False
    ),
    html.Br(),
    dbc.Jumbotron(children=[
    html.H1('Détection d\'animaux'),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'glisser-déposer ou ',
            html.A('sélectionner des fichiers')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'color': 'red',
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Br(),
    html.Div(children=[
        html.H5('Le modèle a détecté l\'animal suivant : '),
        html.P(id='output-data-upload')],
         style={'color': 'black'}),
    
    ])
])

def parse_contents(contents, filename):
    return html.Div([
        html.H5(filename),
        html.Img(src=contents),
        html.Hr()
    ])

TEMP_DIR = r'C:\Users\straw\Desktop\AIS\ProjectPool 2\Classification-images\Output\temp'

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

def save_file(name, content):
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(TEMP_DIR, name), "wb") as file:
        file.write(base64.decodebytes(data))
