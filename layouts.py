# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:07:33 2021

@author: straw
"""
import os
import base64
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from pathlib import Path


layout1 = html.Div(children=[
    html.Div(className="welcome-page-title", children=[html.P('Bienvenue sur l\'Arche de Noé')]),
    html.Br(),
    dbc.Button(dcc.Link('Labellisation', href='/app2'), color="warning", className="btn btn-primary"),
    dbc.Button(dcc.Link('Catalogue', href='/app3'), color="warning", className="btn btn-primary")
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
        dbc.NavItem(dbc.NavLink("Catalogue d'images", href="/app3")),
    ],
    brand="L'Arche de Noé",
    brand_href="/",
    color="primary",
    dark=True
    ),
    html.Br(),
    html.H1('Détection d\'animaux', className="display-4"),
    dbc.Jumbotron(children=[
    dcc.Upload(
        id='upload-image',
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
    html.Div(id='output-image-upload'),
    html.Br(),
    html.Div(children=[
        html.H5('Le modèle a détecté l\'animal suivant : '),
        html.H5(id='output-prediction', className="my-4", style={"font-weight": "bold"})]),
    
    ])
])

def parse_contents(contents, filename):
    return html.Div([
        html.H5(filename),
        html.Img(src=contents),
        html.Hr()
    ])

TEMP_DIR = Path('Output\Mimoun')
TEMP_DIR.mkdir(exist_ok=True, parents=True)

def save_file(name, content):
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(TEMP_DIR, name), "wb") as file:
        file.write(base64.decodebytes(data))

layout3 = html.Div([
    dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Accueil", href="/")),
        dbc.NavItem(dbc.NavLink("Labellisation d'images", href="/app2")),
    ],
    brand="L'Arche de Noé",
    brand_href="/",
    color="primary",
    dark=True
    ),
    html.Br(),
    dbc.Jumbotron(children=[
    html.H1('Catalogue d\'images', className="display-4"),
    html.Br(),
    html.Div([
    dcc.Textarea(id='textarea-state-example',
                 maxLength = 10,
                 minLength = 3,
                 style={'width': '20%', 'height': 60},
    ),
    html.Br(),
    dbc.Button('search', id='textarea-state-example-button', n_clicks=0, color="warning", className="btn btn-primary"),
    html.H5(id='textarea-state-example-output', className="my-4", style={'whiteSpace': 'pre-line'})
    ])
    ])
    ])




