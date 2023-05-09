from dash import *
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests


def create_figure_about():
    df_target = pd.read_csv("model_params/target_csv2", index_col="time", parse_dates=True)
    overview_time_series = px.line(x=df_target.index, y=df_target["price actual"])
    overview_time_series.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    overview_time_series.update_traces(line_color='#fbaf7b')
    overview_time_series.update_xaxes(title_text="Time")
    overview_time_series.update_yaxes(title_text="Price of energy Euro/MW")

    return overview_time_series


def create_figure_map():
    key = "2635ce7e37c34279ac2170036230905"
    countries = ["Valencia", "Bilbao", "Madrid"]
    related_info = list()
    for country in countries:
        api_key = "http://api.weatherapi.com/v1/current.json?key=" + key + "&q=" + country
        if (country == countries[0]):
            api_key = api_key + ",ES"
        response = requests.get(api_key)
        related_info.append(response.json())
        city, lat, lon, condition, precip, wind_mph, pressure, temp = list(), list(), list(), list(), list(), list(), list(), list()

        for weather_condition in related_info:
            city.append(weather_condition["location"]["name"])
            lat.append(weather_condition["location"]["lat"])
            lon.append(weather_condition["location"]["lon"])
            condition.append(weather_condition["current"]["condition"]["text"])
            precip.append(weather_condition["current"]["precip_mm"])
            wind_mph.append(weather_condition["current"]["wind_mph"])
            pressure.append(weather_condition["current"]["pressure_mb"])
            temp.append(weather_condition["current"]["temp_c"])

    data = {"city": city, "lat": lat, "lon": lon, "condition": condition, "precip_mm": precip, "wind_mph": wind_mph,
            "temperature": temp, "pressure_mb": pressure}
    dataset = pd.DataFrame(data)

    # Define the DataFrame with city data
    city_data = data

    df = pd.DataFrame(city_data)

    # Create the choropleth map
    fig = px.choropleth_mapbox(df,
                               geojson='https://raw.githubusercontent.com/deldersveld/topojson/master/countries/spain/spain-comunidad-with-canary-islands.json',
                               locations=df.index,
                               mapbox_style='carto-positron', zoom=5.5,
                               center={'lat': 41.2085, 'lon': -3.713},
                               opacity=0.5)

    # Add the city markers to the map
    fig.add_scattermapbox(lat=df['lat'], lon=df['lon'], hoverinfo='text',
                          text=df['city'] + '<br>' + 'Pressure: ' + df['pressure_mb'].astype(str) + ' mb' + '<br>' +
                               'Precipitation: ' + df['precip_mm'].astype(str) + ' mm' + '<br>' +
                               'Temperature: ' + df['temperature'].astype(str) + ' °C' + '<br>' +
                               'Wind: ' + df['wind_mph'].astype(str) + 'mph' + '<br>' + 'Condition: ' + df['condition'],
                          marker=dict(size=28, color='#fbaf7b', opacity=0.8))

    # Update the layout
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, title={'text': 'Weather informations about cities'},showlegend=False)

    # Show the map
    return fig
