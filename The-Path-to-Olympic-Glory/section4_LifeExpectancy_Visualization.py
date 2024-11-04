import pandas as pd
import plotly.graph_objs as go
from plotly.graph_objs import Figure
import plotly.offline as pyo
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the dataset
df = pd.read_csv('Olympic_Medals_Final_1960-2020.csv')

# Filter relevant columns and drop missing values
filtered_data = df[['LifeExpectancy', 'MedalTotal', 'Country_Name', 'Region', 'Year']].dropna()

# Prepare the data for linear regression
X = filtered_data[['LifeExpectancy']].values
y = filtered_data['MedalTotal'].values

# Perform linear regression
model = LinearRegression()
model.fit(X, y)

# Generate predictions for the regression line
x_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred = model.predict(x_range)

# Calculate the R-squared and correlation coefficient
r_squared = model.score(X, y)
correlation_coefficient = np.corrcoef(filtered_data['LifeExpectancy'], filtered_data['MedalTotal'])[0, 1]

# Pre-defined color palette for regions
colors = {
    "Europe & Central Asia": "#636EFA",
    "North America": "#EF553B",
    "East Asia & Pacific": "#00CC96",
    "South Asia": "#AB63FA",
    "Middle East & North Africa": "#FFA15A",
    "Sub-Saharan Africa": "#19D3F3",
    "Latin America & Caribbean": "#FF6692"
}

# Create the figure
fig = Figure()

# Add scatter plots for each region with unique colors
for region in filtered_data['Region'].unique():
    region_data = filtered_data[filtered_data['Region'] == region]
    fig.add_trace(
        go.Scatter(
            x=region_data['LifeExpectancy'],
            y=region_data['MedalTotal'],
            mode='markers',
            marker=dict(size=8, color=colors.get(region, "#B6E880"), opacity=0.7),
            text=[
                f"Country: {row['Country_Name']}<br>"
                f"Region: {row['Region']}<br>"
                f"Year: {row['Year']}<br>"
                f"Life Expectancy: {row['LifeExpectancy']:.2f}<br>"
                f"Total Medals: {row['MedalTotal']}"
                for _, row in region_data.iterrows()
            ],
            hoverinfo='text+x+y',
            name=region
        )
    )

# Add the regression line
fig.add_trace(
    go.Scatter(
        x=x_range.flatten(),
        y=y_pred,
        mode='lines',
        line=dict(color='black', width=2),
        name=f"Regression line: r = {correlation_coefficient:.2f}"
    )
)

# Customize the layout
fig.update_layout(
    title='Life Expectancy vs Total Medals Won',
    xaxis_title='Life Expectancy in Years',
    yaxis_title='Total Medals Won',
    showlegend=True
)

# Display the plot
pyo.plot(fig, filename='life_expectancy_vs_medals.html')