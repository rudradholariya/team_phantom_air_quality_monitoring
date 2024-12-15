import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Air quality levels in different cities
data = {
    "City": ["City A", "City B", "City C", "City D", "City E"],
    "PM2.5": [35.4, 42.5, 12.1, 55.3, 28.4],
    "PM10": [154, 178, 82, 255, 130]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate AQI status for PM2.5 and PM10
def aqi_status_pm25(value):
    if value <= 12: return "Good"
    elif value <= 35.4: return "Moderate"
    elif value <= 55.4: return "Unhealthy"
    else: return "Very Unhealthy"

def aqi_status_pm10(value):
    if value <= 54: return "Good"
    elif value <= 154: return "Moderate"
    elif value <= 254: return "Unhealthy"
    else: return "Very Unhealthy"

df["PM2.5 Status"] = df["PM2.5"].apply(aqi_status_pm25)
df["PM10 Status"] = df["PM10"].apply(aqi_status_pm10)

# Display the DataFrame
print("Air Quality Data:")
print(df)

# Visualize PM2.5 and PM10 levels
x = np.arange(len(df["City"]))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

# Bar plots for PM2.5 and PM10
bar1 = ax.bar(x - width/2, df["PM2.5"], width, label="PM2.5", color="blue")
bar2 = ax.bar(x + width/2, df["PM10"], width, label="PM10", color="orange")

# Add labels, title, and legend
ax.set_xlabel("City")
ax.set_ylabel("Concentration (µg/m³)")
ax.set_title("PM2.5 and PM10 Levels in Cities")
ax.set_xticks(x)
ax.set_xticklabels(df["City"], rotation=45)
ax.legend()

# Display value labels on bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset text above the bar
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bar1)
add_labels(bar2)

plt.tight_layout()
plt.show()
