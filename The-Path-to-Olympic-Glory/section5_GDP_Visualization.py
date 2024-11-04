import pandas as pd
import plotly.graph_objs as go
import numpy as np
from scipy.stats import linregress
import plotly.colors as pc


# Load the dataset
data = pd.read_csv('Olympic_Medals_Final_1960-2020.csv')

# Filter out rows with missing GDP, MedalTotal, or Region values
filtered_data = data.dropna(subset=['GDP', 'MedalTotal', 'Region'])

# Fit the linear regression model on absolute GDP values
slope, intercept, r_value, p_value, std_err = linregress(
    filtered_data['GDP'], filtered_data['MedalTotal']
)

# Generate points for the regression line
gdp_min, gdp_max = filtered_data['GDP'].min(), filtered_data['GDP'].max()
gdp_range = np.linspace(gdp_min, gdp_max, 100)  # 100 points between min and max GDP
regression_line_y = slope * gdp_range + intercept  # Calculate y values for regression line

# Choose a vibrant color palette
vibrant_colors = pc.qualitative.Bold  # Try Plotly, Bold, or Prism for vibrant options

# Initialize the figure
fig = go.Figure()

# Get the unique list of regions
regions = filtered_data['Region'].unique()

# Assign colors to regions using the vibrant palette
color_mapping = {region: vibrant_colors[i % len(vibrant_colors)] for i, region in enumerate(regions)}

# Create scatter plots for each region with unique vibrant colors
for region in regions:
    region_data = filtered_data[filtered_data['Region'] == region]
    fig.add_trace(go.Scatter(
        x=np.log10(region_data['GDP']),  # Log scale for plotting
        y=region_data['MedalTotal'],
        mode='markers',
        name=region,
        marker=dict(size=8, opacity=0.7, color=color_mapping[region]),
        text=region_data['Country_Name'] + ' (' + region_data['Year'].astype(str) + ')'
    ))

# Plot the regression line (using log-transformed x-axis values for plotting)
fig.add_trace(go.Scatter(
    x=np.log10(gdp_range),  # Log scale for the x-axis
    y=regression_line_y,
    mode='lines',
    line=dict(color='black', width=2),
    name=f'Regression line (fitted on raw values): r = {r_value:.2f}'
))

# Customize the layout
fig.update_layout(
    title="GDP vs Total Medals Won (X-axis in Log Scale)",
    xaxis_title="Log(GDP) - log10 scale",
    yaxis_title="Total Medals Won",
    showlegend=True
)

# Display the plot
fig.show()