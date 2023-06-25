import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Prompt the user for the JSON file name
json_file = input("Enter the JSON file name: ")

# Read the JSON file
with open(json_file) as file:
    json_data = file.read()

# Parse the JSON data
data = json.loads(json_data)

# Extract location names and result values
locations = [item['location'] for item in data]
results = [item['result'] for item in data]

# Sort the locations and results based on results in ascending order
sorted_data = sorted(zip(results, locations))
results, locations = zip(*sorted_data)

# Define the color map
colors = ['green', 'yellow', 'red']
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

# Create a custom color palette for the graph
color_palette = cmap(np.linspace(0, 1, len(results)))

# Create a bar plot with custom colors
plt.figure(figsize=(10, 6))
plt.bar(locations, results, color=color_palette)

plt.xlabel('Location')
plt.ylabel('Result')
plt.title('Results by Location')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()