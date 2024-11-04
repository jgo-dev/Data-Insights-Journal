import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

cars_data = pd.read_csv('cars.csv')

# Analysis for Section 1: Introduction - Setting the Stage

# 1. Descriptive Statistics
# Total number of cars
total_cars = cars_data.shape[0]

# Range of years (earliest to latest models)
earliest_year = cars_data['Identification.Year'].min()
latest_year = cars_data['Identification.Year'].max()

# Most frequent car makes
most_frequent_makes = cars_data['Identification.Make'].value_counts().head(5)

# Average City and Highway MPG
average_city_mpg = cars_data['Fuel Information.City mpg'].mean()
average_highway_mpg = cars_data['Fuel Information.Highway mpg'].mean()

# 2. Visualizations
# Histogram of Cars by Year
trace = go.Histogram(
    x=cars_data['Identification.Year'],
    nbinsx=latest_year - earliest_year + 1,  # Set number of bins to match year range
    marker=dict(color='rgba(0,0,255,0.7)'),
)
layout = go.Layout(
    title='Distribution of Vehicles by Year',
    xaxis=dict(
        title='Model Year',
        dtick=1,  # Set tick interval to 1
        tick0=earliest_year,  # Start ticks at the earliest year
        range=[earliest_year - 0.5, latest_year + 0.5]  # Extend range slightly
    ),
    yaxis=dict(title='Count of Vehicles'),
    width=800,
    height=600,
)
fig = go.Figure(data=[trace], layout=layout)
pyo.plot(fig, filename="cars_distribution_by_year.html")

# Bar chart for Average MPG by Year
avg_mpg_year = cars_data.groupby('Identification.Year')[['Fuel Information.City mpg', 'Fuel Information.Highway mpg']].mean()

trace1 = go.Bar(
    x=avg_mpg_year.index,
    y=avg_mpg_year['Fuel Information.City mpg'],
    name='City MPG',
)
trace2 = go.Bar(
    x=avg_mpg_year.index,
    y=avg_mpg_year['Fuel Information.Highway mpg'],
    name='Highway MPG',
)
layout = go.Layout(
    title='Average City and Highway MPG by Year',
    xaxis=dict(title='Year'),
    yaxis=dict(title='Average MPG'),
    barmode='group',
    width=1000,
    height=600,
)
fig = go.Figure(data=[trace1, trace2], layout=layout)
pyo.plot(fig, filename="average_mpg_by_year.html")

# Summary for blog post output
summary = {
    "Total Cars": total_cars,
    "Model Year Range": (earliest_year, latest_year),
    "Top 5 Makes": most_frequent_makes.to_dict(),
    "Average City MPG": average_city_mpg,
    "Average Highway MPG": average_highway_mpg
}

# Print summary for easy viewing
print(summary)
