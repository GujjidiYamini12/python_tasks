"""7. Splitting Data for Parallel Processing
A dataset contains the following values:
[5, 10, 15, 20, 25, 30]
Scenario:
You want to distribute the data across 3 processors.
Task:
● Store the data in a NumPy array.
● Split it into 3 equal parts using NumPy.
"""
import numpy as np
ar1=np.array([5, 10, 15, 20, 25, 30])
print(np.array_split(ar1,3))