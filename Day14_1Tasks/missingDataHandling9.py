"""9. Missing Data Handling (NumPy + Pandas)
A dataset:
arr = np.array([10, np.nan, 30, np.nan, 50])
Task:
● Convert to Pandas Series
● Replace NaN values with the mean of the Series
● Print updated data
"""
import numpy as np
import pandas as pd
arr = np.array([10, np.nan, 30, np.nan, 50])
S = pd.Series(arr)
print(S)
mean_s=np.mean(S)
print(mean_s)
S=S.fillna(mean_s)
print(S)