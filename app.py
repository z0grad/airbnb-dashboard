from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

# Import custom modules
import graphs
import components

# Load dataset
df = pd.read_csv("cleaned_airbnb.csv")

# Initialize Dash app with Bootstrap and Google Fonts
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, components.GOOGLE_FONTS_URL])
app.title = "NYC Airbnb Analysis"
server = app.server

# Define app layout
app.layout = dbc.Container([
    # Header with Logo & Title
    dbc.Row([
        dbc.Col(html.Img(src="./assets/airbnb-logo.png", height=50), width="auto"),
        dbc.Col(
            html.H1(
                "NYC Airbnb Analysis",
                style={"fontFamily": components.FONTS["Cursive"],
                       "fontStyle":'Bold', "textAlign": "center", "color": components.COLORS["AIRBNB_RED"]},
            ),
            width="auto",
        ),
    ], justify="center", className="my-4"),
    

    # Tabs Component (Using dbc.Tabs)
    dbc.Tabs(
        id="tabs",
        active_tab="overview",
        children=[
            components.tab("Overview", "overview"),
            components.tab("Price Analysis", "price_analysis"),
            components.tab("Geographical Insights", "geographical_insights"),
        ],
        className="my-3",
        style={"justifyContent": "center",  "width": "auto"},
    ),

    # Tab Content
    html.Div(id="tab-content", children=[], className="p-4")
], fluid=True)

# Callback to update tab content
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab")
)
def render_tab_content(tab_name):
    if tab_name == "overview":
        return dbc.Container([
               

        dbc.Row([
            dbc.Col(components.stats_card("Total Listings", df.shape[0], "./assets/home.png"), md=4),
            dbc.Col(components.stats_card("Total Hosts", df['host_id'].nunique(), "./assets/hosts.png"), md=4),
            dbc.Col(components.stats_card("Total Neighbourhoods", df['neighbourhood'].nunique(), "./assets/location.png"), md=4),
        ]),

            dbc.Row(html.Hr(style={"borderTop": "2px solid #FF5A5F", "margin": "20px"})),

        dbc.Row([

            dbc.Col(dcc.Graph(figure=graphs.bar_top_neighbourhoods(df)), md=6),
            dbc.Col(dcc.Graph(figure=graphs.pie_neighbourhood_group(df)), md=3),
            dbc.Col(dcc.Graph(figure=graphs.pie_room_type(df)), md=3),

           
        ]),
    ])

    
    elif tab_name == "price_analysis":
        return dbc.Row([
            dbc.Col(dcc.Graph(figure=graphs.bar_avg_price_neighbourhood_group(df)), md=6),
            dbc.Col(dcc.Graph(figure=graphs.bar_avg_price_neighbourhood(df)), md=6),

            dbc.Row(html.Hr(style={"borderTop": "2px solid #FF5A5F", "margin": "20px"})),

            dbc.Col(dcc.Graph(figure=graphs.bar_avg_price_room_type(df)), md=6),
            dbc.Col(dcc.Graph(figure=graphs.heatmap_median_price(df)), md=6),
        ])

    elif tab_name == "geographical_insights":
        return dbc.Row([
            dbc.Col(dcc.Graph(figure=graphs.scatter_neighbourhood_map(df)), md=6),
            dbc.Col(dcc.Graph(figure=graphs.scatter_neighbourhood_price(df)), md=6),
        ])
    
    return html.P("Select a tab to view data.", className="text-center")

# Run the app
if __name__ == "__main__":
    app.run( port=8080, debug=True)
