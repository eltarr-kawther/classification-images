# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:23:16 2021

@author: straw
"""
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server
from layouts import layout1, layout2
import callbacks

from rgb2graytransformer import RGB2GrayTransformer
from hogtransformer import HogTransformer

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
         return layout1
    elif pathname == '/app2':
         return layout2
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)

