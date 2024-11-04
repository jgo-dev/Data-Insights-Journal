import plotly.graph_objs as go
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.offline as pyo

# Load the data
cars_data = pd.read_csv('cars.csv')

# Function to create regression line
def add_regression_line(x, y):
    X = x.values.reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)
    line_x = np.array([x.min(), x.max()]).reshape(-1, 1)
    line_y = model.predict(line_x)
    return line_x.flatten(), line_y

# Scatter Plot: Horsepower vs. City MPG with regression line
hp = cars_data['Engine Information.Engine Statistics.Horsepower']
city_mpg = cars_data['Fuel Information.City mpg']
model_year = cars_data['Identification.Model Year']
line_x, line_y = add_regression_line(hp, city_mpg)

# Calculate correlation coefficient
r_value = np.corrcoef(hp, city_mpg)[0,1]

fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=hp, y=city_mpg,
    mode='markers',
    name='Data Points',
    hovertemplate='Horsepower: %{x}<br>City MPG: %{y}<br>Model Year: %{text}<extra></extra>',
    text=model_year
))
fig1.add_trace(go.Scatter(
    x=line_x, y=line_y,
    mode='lines',
    name=f'Regression Line: r = {r_value:.2f}'
))
fig1.update_layout(
    title='Horsepower vs. City MPG',
    xaxis_title='Horsepower',
    yaxis_title='City MPG'
)
pyo.plot(fig1, filename='horsepower_vs_city_mpg.html')

# Scatter Plot: Horsepower vs. Highway MPG with regression line
highway_mpg = cars_data['Fuel Information.Highway mpg']
line_x, line_y = add_regression_line(hp, highway_mpg)

# Calculate correlation coefficient
r_value = np.corrcoef(hp, highway_mpg)[0,1]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=hp, y=highway_mpg,
    mode='markers',
    name='Data Points',
    hovertemplate='Horsepower: %{x}<br>Highway MPG: %{y}<br>Model Year: %{text}<extra></extra>',
    text=model_year
))
fig2.add_trace(go.Scatter(
    x=line_x, y=line_y,
    mode='lines',
    name=f'Regression Line: r = {r_value:.2f}'
))
fig2.update_layout(
    title='Horsepower vs. Highway MPG',
    xaxis_title='Horsepower',
    yaxis_title='Highway MPG'
)
pyo.plot(fig2, filename='horsepower_vs_highway_mpg.html')


# ... keep existing horsepower plots ...

# Scatter Plot: Torque vs. City MPG with regression line
torque = cars_data['Engine Information.Engine Statistics.Torque']
city_mpg = cars_data['Fuel Information.City mpg']
model_year = cars_data['Identification.Model Year']
line_x, line_y = add_regression_line(torque, city_mpg)

# Calculate correlation coefficient
r_value = np.corrcoef(torque, city_mpg)[0,1]

fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=torque, y=city_mpg,
    mode='markers',
    name='Data Points',
    hovertemplate='Torque: %{x}<br>City MPG: %{y}<br>Model Year: %{text}<extra></extra>',
    text=model_year
))
fig3.add_trace(go.Scatter(
    x=line_x, y=line_y,
    mode='lines',
    name=f'Regression Line: r = {r_value:.2f}'
))
fig3.update_layout(
    title='Torque vs. City MPG',
    xaxis_title='Torque',
    yaxis_title='City MPG'
)
pyo.plot(fig3, filename='torque_vs_city_mpg.html')

# Scatter Plot: Torque vs. Highway MPG with regression line
highway_mpg = cars_data['Fuel Information.Highway mpg']
line_x, line_y = add_regression_line(torque, highway_mpg)

# Calculate correlation coefficient
r_value = np.corrcoef(torque, highway_mpg)[0,1]

fig4 = go.Figure()
fig4.add_trace(go.Scatter(
    x=torque, y=highway_mpg,
    mode='markers',
    name='Data Points',
    hovertemplate='Torque: %{x}<br>Highway MPG: %{y}<br>Model Year: %{text}<extra></extra>',
    text=model_year
))
fig4.add_trace(go.Scatter(
    x=line_x, y=line_y,
    mode='lines',
    name=f'Regression Line: r = {r_value:.2f}'
))
fig4.update_layout(
    title='Torque vs. Highway MPG',
    xaxis_title='Torque',
    yaxis_title='Highway MPG'
)
pyo.plot(fig4, filename='torque_vs_highway_mpg.html')