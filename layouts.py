# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:07:33 2021

@author: straw
"""
import dash_core_components as dcc
import dash_html_components as html

layout1 = html.Div([
    html.H3('Welcome'),
    dcc.Link('Go to App 2', href='/apps/app2')
])

layout2 = html.Div([
    html.H3('App 2'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/')
])