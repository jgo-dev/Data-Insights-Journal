import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Load the dataset (replace with your file path if needed)
file_path = "State_Total_Years.csv"
bds_data = pd.read_csv(file_path)

# Calculate sums and perform division
state_averages = bds_data[bds_data['Year']=='Avg'].sort_values(
    by='Data.Calculated.Net Job Creation Rate',
    ascending=True
)
sorted_states = state_averages['State_Name'].tolist()

# Prepare data for the heat map
heatmap_data = bds_data.pivot_table(
    values='Data.Calculated.Net Job Creation Rate',
    index='State_Name',
    columns='Year'
).round(2)

# Reorder the rows based on average net job creation rate (reversed order)
heatmap_data = heatmap_data.reindex(sorted_states)

# Create heatmap using plotly
heatmap_fig = go.Figure(data=go.Heatmap(
    z=heatmap_data.values,
    x=heatmap_data.columns,
    y=heatmap_data.index,
    colorscale=[
        [0, 'rgb(255,0,0)'],      # Red for lowest values
        [0.5, 'rgb(255,255,0)'],  # Yellow for middle values
        [1, 'rgb(0,255,0)']       # Green for highest values
    ],
    text=heatmap_data.values,
    texttemplate='%{text:.0f}',
    textfont={"size": 8},
    showscale=True,
    colorbar=dict(title='Net Job Creation Rate (%)')
))

heatmap_fig.update_layout(
    title="""
    U.S. States Net Job Creation Rate (%) from 1978-2022: <br>
    States sorted in order by Average Net Job Creation Rate (All Years)""",
    xaxis_title='Year',
    yaxis_title='State (Sorted Highest ↑ to Lowest ↓)',  # Modified axis title
    height=900,
    width=1200,
    yaxis={'side': 'left'},
    annotations=[
        dict(
            x=-0.19,  # Position before y-axis
            y=1,      # Top of the plot
            xref='paper',
            yref='paper',
            text='Highest Avg Rate',
            showarrow=False,
            font=dict(size=8)
        ),
        dict(
            x=-0.19,  # Position before y-axis
            y=0,      # Bottom of the plot
            xref='paper',
            yref='paper',
            text='Lowest Avg Rate',
            showarrow=False,
            font=dict(size=8)
        )
    ]
)

# Save heatmap to HTML file
pyo.plot(heatmap_fig, filename='state_heatmap2.html', auto_open=True)
