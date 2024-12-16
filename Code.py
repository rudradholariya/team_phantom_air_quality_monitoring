import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data_path = 'C:/Users/Shivkumar/Downloads/air_quality_monitoring.csv'  # Replace with your file path
data = pd.read_csv(data_path)

# Bar chart: PM2.5 and PM10 levels per city
x = np.arange(len(data['City']))  # City indices
width = 0.35  # Bar width

fig, ax = plt.subplots(figsize=(10, 6))

# Plot PM2.5 and PM10 levels
bars1 = ax.bar(x - width/2, data['PM2.5'], width, label='PM2.5', color='skyblue')
bars2 = ax.bar(x + width/2, data['PM10'], width, label='PM10', color='salmon')

# Add labels and title
ax.set_xlabel('City')
ax.set_ylabel('Pollution Levels (µg/m³)')
ax.set_title('PM2.5 and PM10 Levels by City')
ax.set_xticks(x)
ax.set_xticklabels(data['City'])
ax.legend()

# Show bar values
def add_bar_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, f'{height:.1f}', ha='center', va='bottom')

add_bar_labels(bars1)
add_bar_labels(bars2)

plt.tight_layout()
plt.show()

# Pie chart: Distribution of PM2.5 Status
pm25_status_counts = data['PM2.5 Status'].value_counts()

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(pm25_status_counts, labels=pm25_status_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
ax.set_title('Distribution of PM2.5 Status')

plt.show()

# Pie chart: Distribution of PM10 Status
pm10_status_counts = data['PM10 Status'].value_counts()

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(pm10_status_counts, labels=pm10_status_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
ax.set_title('Distribution of PM10 Status')

plt.show()
