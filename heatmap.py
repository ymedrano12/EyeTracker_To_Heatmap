import pandas as pd
import numpy as np
import scipy.ndimage # type: ignore
import seaborn as sns
import matplotlib.pyplot as plt

# Load gaze data
data = pd.read_csv("gaze_data.csv")

# Smoothing Function (You can choose any of the methods: moving average, Gaussian, or exponential)
def gaussian_smooth(data, sigma=2):
    """Applies Gaussian smoothing to gaze data."""
    data["x"] = scipy.ndimage.gaussian_filter1d(data["x"], sigma=sigma)
    data["y"] = scipy.ndimage.gaussian_filter1d(data["y"], sigma=sigma)
    return data

# Apply smoothing
smoothed_data = gaussian_smooth(data, sigma=5)

# Generate a 2D histogram (binned gaze points) after smoothing
heatmap_data = np.histogram2d(smoothed_data["x"], smoothed_data["y"], bins=50, range=[[0, 1920], [0, 1080]])

# Create heatmap using seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data[0].T, cmap="YlGnBu", cbar=True, xticklabels=False, yticklabels=False)
plt.title("Smoothed Gaze Heatmap")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.show()

# Optionally, save smoothed gaze data to a new CSV file
smoothed_data.to_csv("gaze_data_smoothed.csv", index=False)
