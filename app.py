# Import packages
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import graphs
import components
import pandas as pd

# Load data
df = pd.read_csv('cleaned_airbnb.csv')

# Initialize the app with Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])  # Try FLATLY, LUX, or CYBORG for a dark theme
server = app.server

# App layout
app.layout = dbc.Container(fluid=True, children=[
    
    # Title Section
    dbc.Row(
        dbc.Col(
            html.H1('Airbnb NYC 2019 Analysis', 
                    className="text-center text-primary fw-bold mt-4"), 
            width=12
        )
    ),
    
    html.Hr(className="my-4"),  # Stylish horizontal line

    # Tabs Section
    dbc.Row(
        dbc.Col(
            dcc.Tabs(id='tabs-input', value='overview-tab', children=[
                dcc.Tab(label='🏡 Overview', value='overview-tab', className="fw-bold"),
                dcc.Tab(label='💰 Price Analysis', value='price-tab', className="fw-bold"),
                dcc.Tab(label='🌍 Geographic Analysis', value='geo-tab', className="fw-bold")
            ], className="mb-4"),  # Added margin for spacing
            width=12
        )
    ),

    html.Div(id='tabs-output')  # Placeholder for content

], className="px-4")  # Added padding for better spacing

# Callback function for tabs
@app.callback(
    Output(component_id='tabs-output', component_property='children'),
    Input(component_id='tabs-input', component_property='value')
)
def render_content(tab):    
    if tab == 'overview-tab':
        return components.overview()
    
    elif tab == 'price-tab':
        return components.price_analysis()
    
    elif tab == 'geo-tab':
        return components.geo_analysis()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
