import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from matplotlib.patches import Polygon as MplPolygon

from utils.geometry import mean_centroid




# Generate random points for two triangles
np.random.seed(42)  # For reproducibility


N_REPS = 100000
areas = []

for _ in range(N_REPS):
    triangle1_points = np.random.rand(3, 2)
    triangle2_points = np.random.rand(3, 2)

    # Calculate centroids
    centroid1 = mean_centroid(triangle1_points)
    centroid2 = mean_centroid(triangle2_points)

    # Align the centroids of the triangles to the origin (0,0)
    triangle1_aligned = triangle1_points - centroid1
    triangle2_aligned = triangle2_points - centroid2

    # Create Polygons for overlap calculation
    polygon1 = Polygon(triangle1_aligned)
    polygon2 = Polygon(triangle2_aligned)

    # Find the overlap
    overlap = polygon1.intersection(polygon2)

    PLOT = False
    if PLOT:
        # Plotting
        fig, ax = plt.subplots()
        # Plot triangle 1
        triangle1_patch = MplPolygon(triangle1_aligned, color='blue', alpha=0.5, label='Triangle 1')
        ax.add_patch(triangle1_patch)
        # Plot triangle 2
        triangle2_patch = MplPolygon(triangle2_aligned, color='red', alpha=0.5, label='Triangle 2')
        ax.add_patch(triangle2_patch)

        # Check if there's an overlap and plot it
        if not overlap.is_empty:
            overlap_coords = np.array(overlap.exterior.coords)
            overlap_patch = MplPolygon(overlap_coords, color='green', alpha=0.5, label='Overlap')
            ax.add_patch(overlap_patch)

        # Setting the plot
        ax.relim()
        ax.autoscale_view()
        ax.axhline(0, color='black', linewidth=0.8)
        ax.axvline(0, color='black', linewidth=0.8)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axhline(0, color='grey', lw=1)
        plt.axvline(0, color='grey', lw=1)
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()

    # Return the area of the overlap if it exists, else return 0
    overlap_area = overlap.area if not overlap.is_empty else 0
    areas.append(overlap_area)

plt.hist(areas, bins=1000, density=True)
plt.show()
