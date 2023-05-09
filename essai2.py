import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Define the layout for the home page
home_layout = html.Div(
    children=[
        html.H1('Home Page'),
        html.P('This is the home page.'),
        dcc.Link('Go to Page 1', href='/page-1'),
        html.Br(),
        dcc.Link('Go to Page 2', href='/page-2')
    ]
)

# Define the layout for page 1
page1_layout = html.Div(
    children=[
        html.H1('Page 1'),
        html.P('This is page 1.'),
        dcc.Link('Go to Home', href='/'),
        html.Br(),
        dcc.Link('Go to Page 2', href='/page-2')
    ]
)

# Define the layout for page 2
page2_layout = html.Div(
    children=[
        html.H1('Page 2'),
        html.P('This is page 2.'),
        dcc.Link('Go to Home', href='/'),
        html.Br(),
        dcc.Link('Go to Page 1', href='/page-1')
    ]
)

# Define the app layout and callbacks
app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        html.Nav(
            children=[
                dcc.Link('Home', href='/'),
                html.Span(' | '),
                dcc.Link('Page 1', href='/page-1'),
                html.Span(' | '),
                dcc.Link('Page 2', href='/page-2')
            ]
        ),
        html.Div(id='page-content')
    ]
)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page1_layout
    elif pathname == '/page-2':
        return page2_layout
    else:
        return home_layout

if __name__ == '__main__':
    app.run_server(debug=True)
