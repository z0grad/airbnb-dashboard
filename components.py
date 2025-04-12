import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
import plotly.express as px
import graphs

df = pd.read_csv('cleaned_airbnb.csv')


def card(img_src, title, number, bg_color="#d4a9a1", text_color="black"):
    return dbc.Card(
        [
            dbc.CardImg(
                src=img_src, 
                top=True, 
                className="mx-auto d-block mt-3",  
                style={'height': '60px', 'width': '60px', 'object-fit': 'contain'}
            ),  

            dbc.CardBody([
                html.H4(title, className="card-title fw-bold", style={'color': text_color}),  

                # Number formatting with comma separator
                html.P(f"{number:,.0f}", className="card-text fw-bold", 
                       style={'color': text_color, 'fontSize': '24px'})  
            ])
        ],
        style={
            "width": "18rem", 
            "textAlign": "center", 
            "backgroundColor": bg_color, 
            "borderRadius": "10px",  
            "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)"
        }
    )


def overview():
    return dbc.Container([
            html.Br(),

            # Row for Cards (Small Gap)
            dbc.Row([
                dbc.Col(card('./assets/home.png', 'Total Listings', df.shape[0]), width=3, className="px-1"),
                dbc.Col(card('./assets/hosts.png', 'Total Hosts', 37457), width=3, className="px-1"),
                dbc.Col(card('./assets/location.png', 'Total Neighbourhoods', df.neighbourhood.nunique()), width=3, className="px-1"),
            ], className='justify-content-center align-items-center text-center g-1'),  # Small gap

            html.Br(),

            # Row for Graphs (Even Layout)
            dbc.Row([
                dbc.Col(dcc.Graph(id='bar-neighbourhood', figure=graphs.top10_neighbourhoods()), width=4),
                dbc.Col(dcc.Graph(id='pie-neighbourhood', figure=graphs.pie_neighbourhood), width=4),
                dbc.Col(dcc.Graph(id='pie-room-type', figure=graphs.pie_room_type), width=4),
            ], className="mb-4")
        ])

def price_analysis():
    return dbc.Container([
            html.Br(),

            # First Row of Price Analysis Graphs
            dbc.Row([
                dbc.Col(dcc.Graph(id='bar-neighbourhood', figure=graphs.neighbourhood_group_bar), width=6),
                dbc.Col(dcc.Graph(id='bar-room-type', figure=graphs.room_type_bar), width=6),
            ], className="mb-4"),

            # Second Row of Price Analysis Graphs
            dbc.Row([
                dbc.Col(dcc.Graph(id='bar-price', figure=graphs.top10_neighbourhoods_price()), width=6),
                dbc.Col(dcc.Graph(id='bar-price-room-type', figure=graphs.pivot_table()), width=6),
            ])
        ])

def geo_analysis():
    return dbc.Container([
            html.Br(),

            # Map Section
            dbc.Row(
                dbc.Col(
                    dcc.Graph(id='map', figure=graphs.map()),
                    width=12,
                    className="shadow-lg p-3 bg-white rounded"
                )
            )
        ], style={'width': '100%', 'display': 'inline-block'})