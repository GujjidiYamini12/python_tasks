""". Product Rating Normalization
Ratings from different users:
ratings = np.array([2, 3, 4, 5, 1])
Task:
● Normalize ratings to a range 0 to 1 using:
normalized = (value - min) / (max - min)
"""
import numpy as np
ratings = np.array([2, 3, 4, 5, 1])
normalized = (ratings - np.min(ratings)) / (np.max(ratings) - np.min(ratings))
print(normalized)