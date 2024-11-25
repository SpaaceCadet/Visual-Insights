from dash import html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
Model_stacked = html.Div(
    children=[

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
                                                dcc.Link(children=[html.Label('About the Dataset')], href="/about",
                                                         className='no-underline')
                                            ]
                                        ),
                                        html.Li(

                                            children=[
                                                html.I(className='fas fa-chart-bar'),
                                                dcc.Link(children=[html.Label('Vanilla LSTM')], href="/vanilla",
                                                         className='no-underline')

                                            ]
                                        ),
                                        html.Li(
                                            className='selected',
                                            children=[
                                                html.I(className='fas fa-cogs'),
                                                html.Label('Stacked LSTM')
                                            ]
                                        ),

                                        html.Li(
                                            children=[
                                                html.I(className='fas fa-cogs'),
                                                dcc.Link(children=[html.Label('CNN LSTM')], href="/cnn_lstm",
                                                         className='no-underline')
                                            ]
                                        ),html.Li(
                                            children=[
                                                html.I(className='fas fa-cogs'),
                                                dcc.Link(children=[html.Label('Logout')], href="/logout",
                                                         className='no-underline')
                                            ]
                                        )

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

                                        html.Div(),
                                        html.H1('VISUAL INSIGHTS'),
                                        html.Img()
                                    ]
                                ), html.Div(
                                    className='content-data',
                                    children=[dbc.Container(className="text-center",
                                                            children=[
                                                                dbc.Row(
                                                                    dbc.Col(html.U(
                                                                        html.H1("Hourly forecast"))

                                                                    ), style={'width': '100%', 'margin-bottom': '2%'}
                                                                ),
                                                                dbc.Row(
                                                                    [dbc.Col(dbc.Input(id="input_number",value="200",
                                                                                       placeholder="Enter_hours_predict",
                                                                                       type="text"), width=12),
                                                                     dbc.Col(
                                                                         children=[html.H3(
                                                                             "Price of hourly energy price euro/MW"),
                                                                             html.Div(id='predictions_h_1',
                                                                                      style={'width': '100%',
                                                                                             'margin': '0%'})
                                                                         ], width=6),

                                                                     dbc.Col(children=[html.U(html.H3("Distribution")),
                                                                                       html.Div(id='fig_box',
                                                                                                style={'width': '100%',
                                                                                                       'margin': '0%'})],
                                                                             width=6),
                                                                     dbc.Col(children=[
                                                                         html.U(html.H3("Indicateurs de performance")),
                                                                         html.Div(id='fig_table',
                                                                                  style={'width': '100%',
                                                                                         'margin': '0%'})],
                                                                         width=12),
                                                                     ]
                                                                ),
                                                            ],
                                                            fluid=True,
                                                            )])

                            ]
                        )
                    ]
                ),

            ]
        )
    ]
)