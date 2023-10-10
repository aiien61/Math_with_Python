import numpy as np
import pandas as pd

points = np.array([
    [5, 3],
    [3, -4],
    [-2, -4],
    [-3, 5]
])

print(points)

distances = [(points[i, 0] ** 2 + points[i, 1] ** 2)**0.5 for i in range(4)]

re = np.c_[points, distances]
re1 = pd.DataFrame(re)
re1.columns = ['x', 'y', 'distance']
re1.index = ['b', 'g', 'r', 'k']
print(re1)