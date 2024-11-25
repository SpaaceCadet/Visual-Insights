from dash import html
import dash_core_components as dcc

aboutLayout = html.Div(
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
                                            className='selected',
                                            children=[
                                                html.I(className='fas fa-home'),
                                                html.Label('About the Dataset')
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                html.I(className='fas fa-cogs'),
                                                dcc.Link(children=[html.Label('Vanilla LSTM')], href="/vanilla",
                                                         className='no-underline')
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                html.I(className='fas fa-cogs'),
                                                dcc.Link(children=[html.Label('Stacked LSTM')], href="/stacked",
                                                         className='no-underline')
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                html.I(className='fas fa-cogs'),
                                                dcc.Link(children=[html.Label('CNN-LSTM')], href="/cnn_lstm",
                                                         className='no-underline')

                                            ]
                                        ), html.Li(
                                            children=[
                                                html.I(className='bi bi-box-arrow-right', style={"color": "white"}),
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
                                ),
                                html.Div(
                                    className='content-data',
                                    children=[

                                        html.U(html.H1('Hourly Energy forecast using Deep learning Models_db')),
                                        html.Br(),

                                        html.P([html.Br(),
                                                html.U(html.Strong('About the datasets used'))
                                                ]), html.Br(),

                                        html.Ul([
                                            html.Li(
                                                'Hourly_energy: This dataset contains 4 years of electrical consumption, generation, pricing, and weather data for Spain. Consumption and generation data was retrieved from ENTSOE a public portal for Transmission Service Operator (TSO) data. Settlement prices were obtained from the Spanish TSO Red Electric España. Weather data was purchased as part of a personal project from the Open Weather API for the 5 largest cities in Spain and made public here.'),
                                            html.Li(
                                                'The dataset is unique because it contains hourly data for electrical consumption and the respective forecasts by the TSO for consumption and pricing. We focus on predicting electrical comsumption better than the already present forecast in the data.'),
                                            html.Li(
                                                'The purpose of ENTSO-E and ENTSOG is to facilitate the integration of energy markets across Europe, by promoting cooperation and coordination among TSOs and other energy stakeholders. To achieve this goal, ENTSO-E and ENTSOG collect and publish data related to energy production, consumption, transmission, and distribution in their respective regions.'),
                                            html.Li(
                                                'And there is also "weather_data": this dataset contain some statistics about hourly weather conditions.'),
                                            html.Li(
                                                'Weather conditions can significantly impact energy consumption patterns and the availability of renewable energy sources in a certain country. For instance, in countries where winters are cold, there is usually a higher demand for heating, which can increase the demand for natural gas and electricity. Conversely, in countries where summers are hot, there may be an increase in demand for air conditioning, which can lead to increased electricity consumption.'),
                                            html.Li(
                                                'Moreover, weather patterns can impact the production of renewable energy sources such as solar and wind power. For instance, on cloudy or rainy days, solar power output may decrease, and during periods of low wind, wind power generation may also decrease. Therefore, understanding the weather conditions can help energy market analysts and traders make informed decisions about the supply and demand of energy sources, and this information can be incorporated into energy price forecasting Models_db to help anticipate future energy prices.')
                                        ]),

                                        html.P('As an example: (seasonal drought)'),

                                        html.Ul([
                                            html.Li(
                                                'If a country experiences a seasonal drought, it can have an impact on both the price of electricity and water in the bills. Morocco as an example, relies heavily on hydroelectric power generation, a seasonal drought can lead to a decrease in the availability of water, which can impact the production of electricity. This, in turn, can lead to an increase in the price of electricity as the demand for electricity may exceed the supply.'),
                                            html.Li(
                                                'Additionally, a drought can also impact the water supply in your area, which can lead to an increase in the price of water. This is because a decrease in the availability of water can lead to an increase in the cost of extracting and treating water, which can be passed on to the consumer in the form of higher water bills.'),
                                            html.Li(
                                                'Overall, seasonal droughts can have significant impacts on the energy and water sectors, which can be reflected in the prices you pay for electricity and water in your bills.'),
                                            html.Li(
                                                'Generation wind onshore refers to the amount of electrical energy generated by wind turbines that are located on land, as opposed to those located offshore or on bodies of water.'),
                                            html.Li(
                                                'Onshore wind turbines are wind turbines that are located on land, as opposed to offshore wind turbines that are located on water bodies such as oceans or lakes. Onshore wind turbines are often used in areas where there is a suitable wind resource and enough space to install the turbines.'),
                                            html.Li(
                                                '"Total load actual" is a variable in hourly energy demand that represents the total amount of electricity demanded by consumers at a given time.'),
                                            html.Li(
                                                'Electricity demand is the amount of electrical power that consumers require at any given time, and it can vary significantly depending on a number of factors such as the time of day, the day of the week, and the season. "Total load actual" is a measure of the actual electricity demand, expressed in megawatts (MW), at a specific hour of the day.'),
                                            html.Li(
                                                'In an energy dataset, "total load actual" is a crucial variable because it reflects the actual electricity consumption at a given time, and it can be used to analyze consumption patterns, identify trends, and develop energy forecasting Models_db,. Energy demand forecasting is important for energy producers and grid operators as it allows them to plan and adjust their energy supply to meet the demand and avoid energy shortages or overproduction.'),
                                            html.Li(
                                                'If the production costs of electricity from a specific source are higher than the market price, this may indicate that there is a need to invest in research and development to reduce the production costs of that source, or to develop policies that provide incentives for using renewable energy sources.'),
                                            html.Li(
                                                'Additionally, determining the cost of electricity generation from different sources can also help to inform investment decisions and improve the efficiency of energy production. Energy producers can use this information to determine the most cost-effective energy sources to invest in, and to optimize their energy production processes to reduce costs and increase efficiency.'),
                                            html.Li(
                                                'In energy markets, the "day-ahead" price refers to the price of electricity that is agreed upon between energy producers and consumers for the following day. The "price day ahead" variable in an energy dataset represents this day-ahead market price of electricity, which is typically used by energy producers to plan their energy production for the next day and to make pricing decisions.'),
                                            html.Li(
                                                'The "price day ahead" variable is important for energy producers, grid operators, and policymakers, as it provides a forward-looking view of the energy market and allows for better planning and decision-making. It is also a key input for energy forecasting Models_db, which can be used to generate more accurate predictions of energy demand and prices for future periods.'),
                                            html.Li(
                                                '"Generation waste" is a variable in an energy dataset that represents the amount of electrical energy generated from waste materials. Waste materials can include various types of materials such as municipal solid waste, agricultural waste, industrial waste, and others.'),
                                            html.Li('Energies are in (MW/h), speed: m/s, price of energy: euro/MW'),

                                        ]), html.Div(style={'width': '100%', 'height': '500px', 'margin': '0 0 0 0px'},
                                                     children=[dcc.Graph(id='clientside-graph-serie'),

                                                               dcc.Store(
                                                                   id='clientside-store-figure-serie', data={})]),

                                        html.Div([
                                            html.U(html.H3("Current Weather information on the cities")),
                                            html.Br()
                                        ]),
                                        dcc.Graph(
                                            id='clientside-graph-map'
                                        ),
                                        dcc.Store(
                                            id='clientside-store-figure-map', data={}
                                        )
                                    ]

                                )
                            ]
                        )
                    ]
                ),

            ]
        )
    ]
)
