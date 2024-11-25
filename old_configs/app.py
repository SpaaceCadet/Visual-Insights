# index page
import dash_core_components as dcc
from flask_login import logout_user, current_user
from dash.exceptions import PreventUpdate
from dash import *
from Templates import about, loglout, vanilla_lstm, stacked_lstm, Cnn_lstm
from dash.dependencies import Input, Output
# from keras.models import load_model
from inference.model import Model_inference
from serveur import app
import plotly.graph_objects as go
from Figures.Figure_about import create_figure_about, create_figure_map

time_serie = create_figure_about()
fig_map = create_figure_map()
############################################## Instantiate variables ###################################################

# vanilla_model = Model_inference(load_model('./model_params/multivariate_lstm3.h5'))
# stacked_model = Model_inference(load_model('./model_params/multivariate_lstm2.h5'))
# cnn_lstm = Model_inference(load_model('./model_params/multivariate_cnn_lstm.h5'))

vanilla_model = Model_inference("vanillalstm")
stacked_model = Model_inference("varlstm")
cnn_lstm = Model_inference("varcnnlstm")

########################### App layout , will help us in controlling views based on urls ######################
app.layout = html.Div(
    children=[dcc.Store(id='session', storage_type='session'),
              dcc.Location(id='url', refresh=False),

              html.Div(id='page-content', className='content')
              ]
)
########################################## Callbacks ######################################################################

# Callback for loading a new user to the session  based on id

####### Callback For Displaying pages based on the permission level the user has , The default page is login page ######
###### If the user requested the logout page his session will be terminated ################

server = app.server


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return loglout.login
    elif pathname == '/vanilla':
        if current_user.is_authenticated:
            return vanilla_lstm.Model_vanilla

    elif pathname == '/stacked':
        if current_user.is_authenticated:
            return stacked_lstm.Model_stacked
    elif pathname == '/cnn_lstm':
        if current_user.is_authenticated:
            return Cnn_lstm.Mod_hybride
    elif pathname == '/about':
        if current_user.is_authenticated:
            return about.aboutLayout
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return loglout.logout
        else:
            return loglout.logout
    else:
        return '404'


########### Callback to check if the authentification succeded or not if so , the user will be redirected to the login page ########
# Define the callback to update the figures on the about page

# Serverside callback
@app.callback(Output('clientside-store-figure-serie', 'data'),
              Output('clientside-store-figure-map', 'data'),
              [Input('url', 'pathname')])
def update_figures(pathname):
    if pathname == '/about':
        # Return the default figures for other pages
        return time_serie, fig_map
    else:
        raise PreventUpdate


# Serverside callback
# @app.callback(
#     Output('clientside-store-figure', 'data'),
#     Input('shipping-type', 'value'),
# )
# def update_store_data(shipping):
#     dff = df[df['Shipping Mode'] == shipping]
#     stored_figure = px.histogram(dff, x="Customer Segment", y="Sales", color='Department Name')
#     # store hostogram on client side - browser
#     return stored_figure
#
# Clientside callback
app.clientside_callback(
    """
    function(figure_data) {
        if(figure_data === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure_data, {
                'layout': {
                    ...figure_data.layout,
                   
                }
        });
        return fig;
    }
    """,
    Output('clientside-graph-map', 'figure'),
    Input('clientside-store-figure-map', 'data'))

app.clientside_callback(
    """
    function(figure_data, title_text) {
        if(figure_data === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure_data, {
                'layout': {
                    ...figure_data.layout,
                }
        });
        return fig;
    }
    """,
    Output('clientside-graph-serie', 'figure'),
    Input('clientside-store-figure-serie', 'data'))


############################" Callback for running predictions and updating Figures ###########################
@app.callback(Output('predictions_h_1', 'children'),
              Output('fig_box', 'children'),
              Output('fig_table', 'children'),
              [Input('input_number', 'value'), Input('url', 'pathname')])
def predict(input_number, pathname):
    if pathname == '/vanilla':
        performance, forecast, y = vanilla_model.predict(int(input_number), "hourly")
    elif pathname == '/stacked':
        performance, forecast, y = stacked_model.predict(int(input_number), "hourly")
    elif pathname == '/cnn_lstm':
        performance, forecast, y = cnn_lstm.predict(int(input_number), "hourly")
    if ((pathname in ['/vanilla', '/stacked', '/cnn_lstm'])):
        if (input_number == ''):
            input_number = str(0)
        figure = go.Figure()
        figure.add_trace(
            go.Trace(x=[i for i in range(1, int(input_number) + 1)], y=forecast, name="Forecast",
                     marker_color='indianred'))
        figure.add_trace(go.Trace(x=[i for i in range(1, int(input_number) + 1)], y=y, name="Actual values",
                                  marker_color='lightseagreen'))
        figure.update_layout(margin={'l': 0, 'r': 0, 't': 5, 'b': 0}, plot_bgcolor='#ffffcc')

        fig_box = go.Figure()
        fig_box.add_trace(go.Box(y=forecast, name='predictions',
                                 marker_color='indianred'))
        fig_box.add_trace(go.Box(y=y, name='actuals',
                                 marker_color='lightseagreen'))
        fig_box.update_layout(margin={'l': 0, 'r': 0, 't': 5, 'b': 0})
        fig_box.update_layout(
            updatemenus=[
                dict(
                    type="buttons",
                    direction="right",
                    buttons=list([
                        dict(
                            args=["type", "box"],
                            label="box",
                            method="restyle"
                        ),
                        dict(
                            args=["type", "histogram"],
                            label="hist",
                            method="restyle"
                        )]), pad={"r": 10, "t": 10},
                    showactive=False,
                    x=0.5,
                    xanchor="center",
                    y=-0.12,
                    yanchor="bottom")], plot_bgcolor='#ffffcc')
        # figure.update_layout(

        #    title_text='Price of hourly predicted energy price in euro/MW'
        # )

        headerColor = 'grey'
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        fig_table = go.Figure(data=[go.Table(
            header=dict(
                values=['<b>Indicateur</b>', '<b>Value</b>'],
                line_color='darkslategray',
                fill_color=headerColor,
                align=['left', 'center'],
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=[
                    [str(k) for k in performance.keys()],
                    [str(val) for val in performance.values()],
                ],
                line_color='darkslategray',
                # 2-D list of colors for alternating rows
                fill_color=[[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor] * 5],
                align=['left', 'center'],
                font=dict(color='darkslategray', size=11)
            ))
        ])
        return dcc.Graph(figure=figure, config={'displayModeBar': False}), dcc.Graph(figure=fig_box,
                                                                                     config={
                                                                                         'displayModeBar': False}), dcc.Graph(
            figure=fig_table, config={'displayModeBar': False})
    else:
        raise PreventUpdate


############################ Running the server ##############################################################


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=5000)
