import plotly.express as px
import pandas as pd

# Load dataset
df = pd.read_csv('cleaned_airbnb.csv')

def create_pie(column_name):
    title = f"{column_name.replace('_', ' ').title()} Distribution"

    fig = px.pie(
        df, names=column_name, title=f"<b>{title}</b>", hole=0.3,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    # Improve label visibility
    fig.update_traces(
        textinfo='percent+label', 
        insidetextorientation='radial'
    )

    # Center title and remove legend
    fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'}, 
        showlegend=False, 
        margin=dict(l=30, r=30, t=50, b=30)
    )

    return fig

def create_bar_chart(column_name):
    title = f"Average Price per {column_name.replace('_', ' ').title()}"

    # Aggregate data
    agg_price = df.groupby(column_name)['price'].median().sort_values(ascending=False)

    # Create bar chart
    fig = px.bar(
        x=agg_price.index, y=agg_price.values,
        title=f"<b>{title}</b>", 
        labels={'x': column_name.replace('_', ' ').title(), 'y': 'Median Price ($)'},
        text=agg_price.values,  # Show values on bars
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    # Format bars & layout
    fig.update_traces(texttemplate='$%{text:.2s}', textposition='outside')
    fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'}, 
        showlegend=False, 
        margin=dict(l=40, r=40, t=50, b=40),
        xaxis=dict(title='', tickangle=45)
    )

    return fig

def top10_neighbourhoods():
    top_10_neighbourhoods = df['neighbourhood'].value_counts().head(10)
    fig = px.bar(
        x=top_10_neighbourhoods.index, y=top_10_neighbourhoods.values,
        title='<b>Top 10 Neighbourhoods</b>', template='presentation',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'},
        margin=dict(l=40, r=40, t=50, b=40)
    )
    return fig

def top10_neighbourhoods_price():
    top_10_neighbourhoods = df.groupby('neighbourhood')['price'].median().sort_values(ascending=False).head(10)
    fig = px.bar(
        x=top_10_neighbourhoods.index, y=top_10_neighbourhoods.values,
        title='<b>Top 10 Neighbourhoods by Median Price</b>', template='presentation',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'},
        margin=dict(l=40, r=40, t=50, b=40)
    )
    return fig

def pivot_table():
    data = pd.pivot_table(df, index='neighbourhood_group', columns='room_type', values='price', aggfunc='median').T

    fig = px.imshow(
        data, text_auto=True, color_continuous_scale="greens",
        width=650, height=400
    )

    # Remove colorbar, update layout
    fig.update_layout(
        title={'text': "<b>Median Price by Neighbourhood & Room Type</b>", 'x': 0.5, 'xanchor': 'center'},
        coloraxis_showscale=False, margin=dict(l=40, r=40, t=50, b=40)
    )

    # Format axes
    fig.update_xaxes(title='', tickangle=45)
    fig.update_yaxes(title='')

    return fig

def map():
    fig = px.scatter(
        df, x='longitude', y='latitude', color='neighbourhood_group', size='price',
        width=800, height=600, opacity=0.6, color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    # Remove Grid and Axis Labels
    fig.update_xaxes(showgrid=False, zeroline=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, zeroline=False, showticklabels=False)
    fig.update_layout(
        title={'text': "<b>Neighbourhood Group Distribution on Map</b>", 'x': 0.5, 'xanchor': 'center'},
        margin=dict(l=40, r=40, t=50, b=40)
    )
    
    return fig

# Generate Figures
pie_neighbourhood = create_pie('neighbourhood_group')
pie_room_type = create_pie('room_type')
neighbourhood_group_bar = create_bar_chart('neighbourhood_group')
room_type_bar = create_bar_chart('room_type')