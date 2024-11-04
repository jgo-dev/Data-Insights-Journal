import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Load the dataset (replace with your file path if needed)
file_path = "BDS_dataset_final.csv"
bds_data = pd.read_csv(file_path)

# Group the data by year to analyze trends
bds_data_grouped = bds_data.groupby("Year").agg(
    total_job_creation=("Data.Job Creation.Count", "sum"),
    total_job_destruction=("Data.Job Destruction.Count", "sum"),
    unemployment=("Data.Unemployment", "sum")  # Add unemployment data
)

# Calculate net job creation over time
bds_data_grouped["net_job_creation"] = (
    bds_data_grouped["total_job_creation"] - bds_data_grouped["total_job_destruction"]
)

# Create traces for each line
trace1 = go.Scatter(
    x=bds_data_grouped.index,
    y=bds_data_grouped["total_job_creation"],
    name="Total Job Creation",
    line=dict(dash='solid',
              color='slateblue')
)

trace2 = go.Scatter(
    x=bds_data_grouped.index,
    y=bds_data_grouped["total_job_destruction"],
    name="Total Job Destruction",
    line=dict(dash='dash',
              color='red')
)

# Add new unemployment trace
trace3 = go.Scatter(
    x=bds_data_grouped.index,
    y=bds_data_grouped["unemployment"],
    name="Unemployment",
    line=dict(dash='dashdot',
              color='magenta')
)

trace4 = go.Scatter(
    x=bds_data_grouped.index,
    y=bds_data_grouped["net_job_creation"],
    name="Net Job Creation",
    line=dict(dash='dot',
              color='limegreen')
)

# Create the layout
layout = go.Layout(
    title="U.S. National Trends in Job Creation, Destruction, and Unemployment (1978-2022)",
    xaxis=dict(title="Year"),
    yaxis=dict(
        title="Number of Jobs / Unemployment",
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='black'
    ),
    showlegend=True,
    template="plotly_white"
)

# Combine traces and layout
fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)

# Display the plot
pyo.plot(fig, filename='job_trends.html')
