from dash import html

import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from serveur import app, Users
from flask_login import login_user
login =  html.Div(children=[dcc.Location(id='url_login', refresh=True),html.Div(className="bg-dark", children=[html.Div(
    className="col-12 position-absolute top-40 start-20 mb-5",
    children=[html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
        html.H1(
            className="text-center",
            style={"color": "#fbaf7b"},
            children=["VISUAL", html.Br(), "INSIGHTS"],
        ),
        html.Div(
            className="row",
            children=[
                html.Div(className="col-3"),
                html.Div(
                    className="col-12 col-md-6",
                    children=[
                        html.Div(
                            className="mw-md py-12 mx-auto",
                            children=[
                                html.Form(
                                    action="",
                                    children=[
                                        html.Div(
                                            className="mb-4",
                                            children=[
                                                html.Label(style={"color":"#fbaf7b"},
                                                    className="form-label fw-bold",
                                                    children=["Username *"],
                                                ),
                                                dcc.Input(
                                                    className="form-control",
                                                    type="text",id='uname-box',

                                                    placeholder="Enter Username",
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="mb-4",
                                            children=[
                                                html.Label(
                                                    className="form-label fw-bold",
                                                    children=["Password *"],
                                                    style={"color":"#fbaf7b"}
                                                ),
                                                dcc.Input(
                                                    className="form-control",
                                                    type="password",id='pwd-box',

                                                    placeholder="*******",
                                                ),
                                            ],
                                        ),
                                        html.A(
                                            className="btn w-100 mb-8 shadow", style={"background-color": "#fbaf7b"},
                                            n_clicks=0,
                                            id='login-button',
                                            children=["Sign In"],
                                        ),
                                    ],
                                )
                            ],
                        )
                    ],
                ),
                html.Div(className="col-4"),
                html.Div(id='output-state',
                    style={"height": "400px", "color": "white", "text-align": "center"},
                    children=[""],
                ),
            ],
        ),
    ],
)]
)])
logout = html.Div([dcc.Location(id='logout', refresh=True),
        html.Br(),html.Br()
        , html.Div(className="mb-1 pt-3 pb-0",style={"text-align":"center","color":"#fbaf7b"},children=[html.H4('You have been logged out - Please login !')])
        , html.Div(className="mt-1 pt-1",children=[login])

    ])



@app.callback(
    Output('url_login', 'pathname')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def successful(n_clicks, input1, input2):
    user = Users.query.filter_by(username=input1).first()
    if user:
        if input2==user.password:
            login_user(user)
            return '/about'

        else:
            pass
    else:
        pass
@app.callback(
    Output('output-state', 'children')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])

def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        user = Users.query.filter_by(username=input1).first()
        if user:
            if input2==user.password:
                return ''
            else:
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''