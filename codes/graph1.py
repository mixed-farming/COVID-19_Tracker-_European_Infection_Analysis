import json
import plotly.graph_objects as go

# Prompt the user for the JSON file name
json_file = input("Enter the JSON file name: ")

# Read the JSON file
with open(json_file) as file:
    json_data = file.read()

# Parse the JSON data
data = json.loads(json_data)

# Extract location names, days_count, and total_diff values
locations = [item['location'] for item in data]
days_count = [item['values']['days_count'] for item in data]
total_diffs = [item['values']['total_diff'] for item in data]

# Create a 3D scatter plot
fig = go.Figure(data=go.Scatter3d(
    x=days_count,
    y=total_diffs,
    z=list(range(len(locations))),
    mode='markers',
    marker=dict(
        size=8,
        color=total_diffs,
        colorscale='Viridis',
        opacity=0.8
    ),
    text=locations
))

# Set axis labels and title
fig.update_layout(scene=dict(
    xaxis=dict(title='Days Count'),
    yaxis=dict(title='Total Difference'),
    zaxis=dict(title='Location')
), title='Total Difference by Location and Days Count')

# Show the plot
fig.show()