import pandas as pd
import numpy as np
import plotly.graph_objs as go
from scipy.stats import linregress


df = pd.read_csv('Olympic_Medals_Final_1960-2020.csv')


# Drop rows with missing values in 'Population', 'MedalTotal', or 'Region'
df_cleaned = df.dropna(subset=['Population', 'MedalTotal', 'Region'])

# Use raw values for regression fitting
x_raw = df_cleaned['Population'].values
y_raw = df_cleaned['MedalTotal'].values

# Combine country name and year for hover text
hover_text = (
    df_cleaned['Country_Name'] + " (" + df_cleaned['Year'].astype(str) + ")"
).values

# Perform linear regression on raw values
slope, intercept, r_value, _, _ = linregress(x_raw, y_raw)
y_pred = slope * x_raw + intercept

# Log-transform x-axis for plotting purposes (visualization only)
x_log = np.log(x_raw)

# Generate data for the trendline
x_range_log = np.linspace(np.min(x_log), np.max(x_log), 500)
x_range_raw = np.exp(x_range_log)
y_range_pred = slope * x_range_raw + intercept

# Print correlation coefficient
print(f"Correlation coefficient (raw values): {r_value:.2f}")

# Plot with region-based colors
fig_log = go.Figure()

# Assign different colors based on regions
for region in df_cleaned['Region'].unique():
    region_data = df_cleaned[df_cleaned['Region'] == region]
    fig_log.add_trace(
        go.Scatter(
            x=np.log(region_data['Population']),
            y=region_data['MedalTotal'],
            mode='markers',
            marker=dict(size=8),
            name=region,
            text=(
                region_data['Country_Name'] + " (" + region_data['Year'].astype(str) + ")"
            ),
            hovertemplate='%{text}<br>Log(Population): %{x}<br>Medals: %{y}',
        )
    )

# Add the regression line
fig_log.add_trace(
    go.Scatter(
        x=x_range_log, y=y_range_pred,
        mode='lines',
        line=dict(color='black', width=2),
        name=f'Regression line (fitted on raw values): r = {r_value:.2f}'
    )
)

# Update layout for the plot
fig_log.update_layout(
    title='Population vs Total Medals Won (X-axis in Log Scale)',
    xaxis_title='Log(Population) - log10 scale',
    yaxis_title='Total Medals Won'
)

# Show the plot
fig_log.show()