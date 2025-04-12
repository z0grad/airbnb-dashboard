import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc


# 🔹 Common Styling for All Graphs
DEFAULT_LAYOUT = {
    "title_font": dict(size=18, family="Arial", color="black", weight="bold"),
    "title_x": 0.5,  # Center Title
    "margin": dict(l=20, r=20, t=50, b=20),
    "showlegend": False,  # Hide Legend by Default
    "paper_bgcolor": "white",
    "plot_bgcolor": "white",
    "autosize": True,
}

DEFAULT_TRACES = {
    "textinfo": "percent+label",
    "textfont": {"size": 12, "color": "white"},    
    "marker": dict(line=dict(color="#FFFFFF", width=2))
}


COLOR_CATEGORICAL = px.colors.qualitative.Set2
COLOR_CONTINUOUS = px.colors.sequential.Redor

# 🔹 Pie Chart: Neighbourhood Group Distribution
def pie_neighbourhood_group(df):
    fig = px.pie(df, names='neighbourhood_group', hole=0.2,  
                 color_discrete_sequence=COLOR_CATEGORICAL)
    fig.update_layout(title="Neighbourhood Group Distribution", **DEFAULT_LAYOUT)
    fig.update_traces(**DEFAULT_TRACES)
    return fig

# 🔹 Pie Chart: Room Type Distribution
def pie_room_type(df):
    fig = px.pie(df, names='room_type', hole=0.2,  
                 color_discrete_sequence=COLOR_CATEGORICAL)
    fig.update_layout(title="Room Type Distribution", **DEFAULT_LAYOUT)
    fig.update_traces(**DEFAULT_TRACES)
    return fig

# 🔹 Bar Chart: Top 10 Neighbourhoods by Listings
def bar_top_neighbourhoods(df):
    top_10 = df['neighbourhood'].value_counts().head(10)
    fig = px.bar(top_10, x=top_10.index, y=top_10.values, 
                 color_discrete_sequence=COLOR_CATEGORICAL)
    fig.update_layout(title="Top 10 Neighbourhoods by Listings", **DEFAULT_LAYOUT,
                      xaxis_title="Neighbourhood", yaxis_title="Number of Listings")
    return fig

# 🔹 Scatter Plot: Neighbourhood Group Distribution on Map
def scatter_neighbourhood_map(df):
    fig = px.scatter(df, x='longitude', y='latitude', color='neighbourhood_group',
                     title='Neighbourhood Group Distribution on Map'
                     , color_discrete_sequence=COLOR_CATEGORICAL)
    fig.update_layout(**DEFAULT_LAYOUT)
    fig.update_xaxes(showgrid=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    return fig

def scatter_neighbourhood_price(df):
    fig = px.scatter(df, x='longitude', y='latitude', color='neighbourhood_group', size = 'price',
                     title='Neighbourhood Group Distribution on Map'
                     , color_discrete_sequence=COLOR_CATEGORICAL)
    fig.update_layout(**DEFAULT_LAYOUT)
    fig.update_xaxes(showgrid=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    return fig

# 🔹 Bar Chart: Average Price per Neighbourhood Group
def bar_avg_price_neighbourhood_group(df):
    avg_price = df.groupby('neighbourhood_group')['price'].median().sort_values(ascending=False)
    fig = px.bar(avg_price, x=avg_price.index, y=avg_price.values,  text=avg_price.values,
                 color_discrete_sequence=COLOR_CATEGORICAL)
    fig.update_layout(
        title="Average Price per Neighbourhood Group",
        **DEFAULT_LAYOUT,
        xaxis_title="",
        yaxis_title="<b>Median Price</b>",  # Bold Y-axis title
    )
    fig.update_traces(
        texttemplate='%{text}',  # Display values inside bars
        textposition='inside',
        textfont=dict(color="white", size=18, family="Arial", )  # Customize text appearance
    )
    
    fig.update_xaxes(tickfont=dict(family="Arial", size=14, color="black", weight="bold"), title='')
    fig.update_yaxes(tickfont=dict(family="Arial", size=14, color="black"))
    return fig


# 🔹 Bar Chart: Average Price per Room Type
def bar_avg_price_room_type(df):
    avg_price = df.groupby('room_type')['price'].median().sort_values(ascending=False)
    fig = px.bar(avg_price, x=avg_price.index, y=avg_price.values, text=avg_price.values,
                 color_discrete_sequence=COLOR_CATEGORICAL)
    
    fig.update_layout(
        title="Average Price per Room Type",
        **DEFAULT_LAYOUT,
        xaxis_title="Room Type",
        yaxis_title="<b>Median Price</b>"  # Bold Y-axis title
    )
    
    fig.update_traces(
        texttemplate='%{text}',  # Display values inside bars
        textposition='inside',
        textfont=dict(color="white", size=18, family="Arial", )  # Customize text appearance
    )
    
    fig.update_xaxes(tickfont=dict(family="Arial", size=14, color="black", weight="bold"), title='')  # Bold X-axis labels
    fig.update_yaxes(tickfont=dict(family="Arial", size=14, color="black"))  # Style Y-axis ticks

    return fig



# 🔹 Bar Chart: Average Price per Neighbourhood (Top 10)
def bar_avg_price_neighbourhood(df):
    avg_price = df.groupby('neighbourhood')['price'].median().sort_values(ascending=False).head(10)
    fig = px.bar(avg_price, x=avg_price.index, y=avg_price.values, text=avg_price.index,
                 color_discrete_sequence=COLOR_CATEGORICAL)
    
    fig.update_layout(
        title="Average Price per Neighbourhood (Top 10)",
        **DEFAULT_LAYOUT,
        xaxis_title="",
        yaxis_title="<b>Median Price</b>"  # Make Y-axis title bold
    )
    
    fig.update_traces(
        textposition='inside',
        textangle=-90,  # Rotate text
        textfont=dict(color="white", size=14, family="Arial"),  # Customize text color, size, font
        insidetextanchor="middle"  # Ensure text is inside the bars
    )
    
    fig.update_xaxes(showticklabels=False)  # Hide x-axis labels
    fig.update_yaxes(tickfont=dict(family="Arial", size=14, color="black"))  # Style Y-axis ticks

    return fig


# 🔹 Treemap: Average Price by Neighbourhood Group & Room Type
def treemap_avg_price(df):
    df_avg = df.groupby(['neighbourhood_group', 'room_type'], as_index=False)['price'].mean()
    fig = px.treemap(df_avg, path=['neighbourhood_group', 'room_type'], values='price',
                      color='price', color_continuous_scale=COLOR_CATEGORICAL)
    fig.update_layout(title="Average Price by Neighbourhood Group and Room Type", **DEFAULT_LAYOUT)
    return fig

# 🔹 Treemap: Number of Listings by Neighbourhood Group & Neighbourhood
def treemap_listings_count(df):
    df_count = df.groupby(['neighbourhood_group', 'neighbourhood'])['neighbourhood'].count().reset_index(name='count')
    fig = px.treemap(df_count, path=['neighbourhood_group', 'neighbourhood'], values='count',
                      color='count', color_continuous_scale=COLOR_CATEGORICAL)
    fig.update_layout(title="Number of Listings by Neighbourhood Group and Neighbourhood", **DEFAULT_LAYOUT)
    return fig

def heatmap_median_price(df):
    data = pd.pivot_table(df, index='neighbourhood_group', columns='room_type', values='price', aggfunc='median').T
    fig = px.imshow(data, text_auto=True, title='Median Price by Neighbourhood Group and Room Type',
                    color_continuous_scale='greens', aspect='auto',
                    )
    fig.update_layout(**DEFAULT_LAYOUT,coloraxis_showscale=False)
    fig.update_xaxes(tickfont=dict(family="Arial", size=14, color="black", weight="bold"),title='')
    fig.update_yaxes(tickfont=dict(family="Arial", size=14, color="black", weight="bold"), title='')
    return fig