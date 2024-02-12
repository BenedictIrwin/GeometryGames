import numpy as np

# Function to calculate the centroid of a polygon
def mean_centroid(points):
    return np.mean(points, axis=0)