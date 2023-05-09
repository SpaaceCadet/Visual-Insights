
from dash import *
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_figure_about():
    df_target = pd.read_csv("model_params/target_csv2", index_col="time", parse_dates=True)
    years = set(df_target.index.year)

    overview_time_series = go.Figure()
    for element in list(df_target.index.year.unique().values):
            slice=df_target.loc[df_target.index.year == int(element)]
            overview_time_series.add_trace(
                go.Trace(x=slice.index, y=slice["price actual"], line=dict(color='#fbaf7b', width=2),name=int(element)))

            overview_time_series.update_layout({'xaxis': {'title': {'text': 'Time'}, 'title_font': dict(size=15)},
                                                'yaxis': {'title': {'text': 'Estimated Price of Energy'},
                                                          'title_font': dict(size=17)}},
                                               plot_bgcolor='white',
                                               paper_bgcolor='white', font_color="black", font_family="Rockwell",
                                               legend=dict(
                                                   orientation="h",
                                                   yanchor="bottom",
                                                   y=1.02,
                                                   xanchor="right",
                                                   x=1, bgcolor="#ffffcc"))

            dropdown_buttons = [
                {'label': 'All years', 'method': 'update',
                 'args': [{'visible': [True, True, True, True,True]},
                          {'title': 'All years '}]},
                {'label': 2014, 'method': 'update',
                 'args': [{'visible': [True, False, False, False,False]},
                          {'title': 'Year :2014'}]},
                {'label': 2015, 'method': 'update',
                 'args': [{'visible': [False, True, False,False, False]},
                          {'title': 'Year :2015'}]},
                {'label': 2016, 'method': 'update',
                 'args': [{'visible': [False, False, True, False,False]},
                          {'title': 'Year :2016'}]},
                {'label': 2017, 'method': 'update',
                 'args': [{'visible': [False, False, False, True,False]},
                          {'title': 'Year :2017'}]},
                {'label': 2018, 'method': 'update',
                 'args': [{'visible': [False, False, False,False, True]},
                          {'title': 'Year :2018'}]}
            ]

            overview_time_series.update_layout({
                'updatemenus': [{
                    'type': "dropdown", 'x': 1.3, 'y': 1, 'showactive': True, 'active': 0,
                    'buttons': dropdown_buttons}]
            })

    return overview_time_series