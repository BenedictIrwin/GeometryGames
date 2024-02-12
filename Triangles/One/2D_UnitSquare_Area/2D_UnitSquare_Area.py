import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from scipy.special import spence as Li2

def P(AA):
    """https://mathworld.wolfram.com/SquareTrianglePicking.html
    
    Note spence (1-z) is Li_2 in Mathematica/Wikipedia definition"""
    array = []
    for A in AA:
        if(A == 0):
            term1 = 0
        else:
            term1 = 12 * (np.log(2*A) - 5) * np.log(2*A) * A**2
        term2 = 24 * (A + 1) * Li2(1 - 2*A) * A
        term3 = -4 * (A + 1) * np.pi**2 * A
        term4 = -6 * A
        if(A == 0.5):
            term5 = 0
        else:
            term5 = 3 * (2*A - 1) * (10*A + 1) * np.log(1 - 2*A)
        term6 = 3
        array.append(4 * (term1 + term2 + term3 + term4 + term5 + term6))
    return np.array(array)

np.random.seed(42)  # For reproducibility

N_REPS = 100000
areas = []

for _ in range(N_REPS):
    triangle1_points = np.random.rand(3, 2)
    polygon1 = Polygon(triangle1_points)
    area = polygon1.area
    areas.append(area)

uniform_A = np.linspace(start=0.0, stop=0.5, num=100)

# x-coord
plt.hist(areas, bins=1000, density=True)
plt.plot(uniform_A, P(uniform_A), '-k')
plt.show()