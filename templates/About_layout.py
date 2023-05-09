from dash import *
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


class LayoutApp:

    def __init__(self):
        self.layout = html.Div(
            children=[
                html.Meta(charSet='UTF-8'),
                html.Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
                html.Title('Side Menu Design By Future Web '),
                html.Div(
                    className='menu-wrapper',
                    children=[
                        html.Div(
                            className='sidebar-header',
                            children=[
                                html.Div(
                                    className='sideBar',
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Img(
                                                    src='https://cdn-03.9rayti.com/rsrc/cache/widen_224/uploads/2012/06/logo-ump-universite-mohammed-premier-oujda.png'
                                                )
                                            ]
                                        ),
                                        html.Ul(
                                            className='unordered_list',
                                            children=[
                                                html.Li(
                                                    children=[
                                                        html.I(className='fas fa-home'),
                                                        html.Label('About the Dataset')
                                                    ]
                                                ),
                                                html.Li(
                                                    children=[
                                                        html.I(className='fas fa-chart-bar'),
                                                        html.Label('Vanilla LSTM')
                                                    ]
                                                ),
                                                html.Li(
                                                    children=[
                                                        html.I(className='fas fa-cogs'),
                                                        html.Label('Stacked LSTM')
                                                    ]
                                                ),
                                                html.Li(
                                                    children=[
                                                        html.I(className='fas fa-phone-alt'),
                                                        html.Label('CNN-LSTM')
                                                    ]
                                                ),

                                            ]
                                        ),
                                        html.Span(
                                            className='cross-icon',
                                            children=[
                                                html.I(className='fas fa-times')
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className='backdrop'
                                ),
                                html.Div(
                                    className='content',
                                    children=[
                                        html.Header(
                                            children=[

                                                html.Div(
                                                    className='menu-button',
                                                    id='desktop',
                                                    children=[
                                                        html.Div(),
                                                        html.Div(),
                                                        html.Div()
                                                    ]
                                                ),
                                                html.Div(
                                                    className='menu-button',
                                                    id='mobile',
                                                    children=[
                                                        html.Div(),
                                                        html.Div(),
                                                        html.Div()
                                                    ]
                                                ),
                                                html.H1('ENSAO VISUAL'),
                                                html.Img()
                                            ]
                                        ),
                                        html.Div(
                                            className='content-data',
                                            children=[

                                            ]

                                        )
                                    ]
                                )
                            ]
                        ),

                        html.Script(src='index.js')
                    ]
                )
            ]
        )
    def get_layout(self):
        pass


class About(LayoutApp):
    def __init__(self):
        LayoutApp.__init__(self)
        unordered_list = self.layout.children[0].children[3].children[0].children[0].children[1].children[0]
        for child in unordered_list.children:
            if isinstance(child, html.Li):
                child.className = ''  # Remove any existing "selected" classes from list items
        unordered_list.children[0].className = 'selected'



    def get_layout(self):
        return self.layout

class Vanilla(LayoutApp):
    def __init__(self):
        LayoutApp.__init__(self)
        unordered_list = self.layout.children[0].children[3].children[0].children[0].children[1].children[0]
        for child in unordered_list.children:
            if isinstance(child, html.Li):
                child.className = ''  # Remove any existing "selected" classes from list items
        unordered_list.children[1].className = 'selected'

    def get_layout(self):
        return self.layout



