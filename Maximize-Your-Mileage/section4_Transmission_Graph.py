import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Read the CSV file
df = pd.read_csv('cars.csv')

# Create separate dataframes for automatic and manual transmissions
auto_df = df[df['Identification.Classification'].str.contains('Automatic', case=False)]
manual_df = df[df['Identification.Classification'].str.contains('Manual', case=False)]

# Calculate mean MPG values for each year
auto_means = auto_df.groupby('Identification.Year').agg({
    'Fuel Information.City mpg': 'mean',
    'Fuel Information.Highway mpg': 'mean'
}).reset_index()

manual_means = manual_df.groupby('Identification.Year').agg({
    'Fuel Information.City mpg': 'mean',
    'Fuel Information.Highway mpg': 'mean'
}).reset_index()

# Create traces for each line
traces = [
        go.Scatter(
        x=manual_means['Identification.Year'],
        y=manual_means['Fuel Information.Highway mpg'],
        mode='lines+markers',
        marker=dict(size=10, symbol='triangle-up'),
        name='Manual - Highway MPG',
        line=dict(color='red')
    ),
        go.Scatter(
        x=auto_means['Identification.Year'],
        y=auto_means['Fuel Information.Highway mpg'],
        mode='lines+markers',
        marker=dict(size=14, symbol='circle'),
        name='Automatic - Highway MPG',
        line=dict(color='blue')
    ),
    go.Scatter(
        x=manual_means['Identification.Year'],
        y=manual_means['Fuel Information.City mpg'],
        mode='lines+markers',
        marker=dict(size=10, symbol='triangle-up'),
        name='Manual - City MPG',
        line=dict(color='red', dash='dot')
    ),
    
    go.Scatter(
        x=auto_means['Identification.Year'],
        y=auto_means['Fuel Information.City mpg'],
        mode='lines+markers',
        marker=dict(size=14, symbol='circle'),
        name='Automatic - City MPG',
        line=dict(color='blue', dash='dot')
    ),


]

# Create layout
layout = go.Layout(
    title='Average MPG Trends by Transmission Type',
    xaxis=dict(title='Year', tickmode='linear'),
    yaxis=dict(title='Miles Per Gallon (MPG)'),
    hovermode='x unified',
    showlegend=True,
    template='plotly_white'
)

# Create figure
fig = go.Figure(data=traces, layout=layout)

# Add gridlines
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

# Show plot
pyo.plot(fig, filename='mpg_trends.html')

