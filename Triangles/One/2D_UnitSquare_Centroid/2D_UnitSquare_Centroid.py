import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb  # For binomial coefficients

def BatesDistribution(x, n):
    """Bates distribution"""
    if (x < 0).any() or (x > 1).any():
        raise ValueError('Elements must be in [0,1]')
    
    sum_term = 0
    for k in range(n + 1):
        term = (-1)**k * comb(n, k) * (n*x - k)**(n-1) * np.sign(n*x - k)
        sum_term += term
    
    return n / (2 * np.math.factorial(n - 1)) * sum_term

# Function to calculate the centroid of a polygon
def mean_centroid(points):
    return np.mean(points, axis=0)

np.random.seed(42)  # For reproducibility

N_REPS = 100000
centroids = []

for _ in range(N_REPS):
    triangle1_points = np.random.rand(3, 2)
    centroid = mean_centroid(points=triangle1_points)
    centroids.append(centroid)

centroids = np.array(centroids)

uniform_x = np.linspace(start=0.0, stop=1.0, num=100)

# x-coord
plt.hist(centroids[:,0], bins=100, density=True)

plt.plot(uniform_x, BatesDistribution(uniform_x, n=3), '-k')
plt.show()
# y-coord
plt.hist(centroids[:,1], bins=100, density=True)
plt.plot(uniform_x, BatesDistribution(uniform_x, n=3), '-k')
plt.show()