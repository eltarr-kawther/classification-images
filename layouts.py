# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:07:33 2021

@author: straw
"""
import dash_core_components as dcc
import dash_html_components as html

layout1 = html.Div(children=[
    html.H1('Welcome'),
    dcc.Link('Go to App 2', href='/apps/app2')
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
    html.H1('App 2'),
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