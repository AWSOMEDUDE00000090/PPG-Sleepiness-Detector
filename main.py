import matplotlib.pyplot as plt
import csv
import plotly.graph_objects as go


with open('TWdata1.csv', 'r') as file:
    reader = csv.reader(file)
    data = [float(value if value != '' else '0') for row in reader for value in row]

# Generate x values with 0.01 seconds interval
time_interval = 0.01
x_values = [i * time_interval for i in range(len(data))]

# Cut out the first 20 seconds and last 5 seconds
start_time = 5
end_time = len(data) * time_interval - 6
filtered_x_values = [t for t in x_values if start_time <= t <= end_time]
filtered_data = [d for t, d in zip(x_values, data) if start_time <= t <= end_time]

# Create a scatter plot with plotly
fig = go.Figure(data=go.Scatter(x=filtered_x_values, y=filtered_data, mode='lines+markers'))

# Customize the plot as needed
fig.update_layout(
    title='PPG Heart Rate',
    xaxis=dict(title='Time (seconds)'),
    yaxis=dict(title='Values'),
    hovermode='closest',
)

# Show the plot
fig.show()