"""Combo of Numpy and Pandas
1. Convert NumPy Array to Pandas Series
A dataset:
arr = np.array([10, 20, 30, 40])
Task:
● Convert this NumPy array into a Pandas Series
● Assign index labels: ["A", "B", "C", "D"]
"""
import numpy as np
import pandas as pd
arr = np.array([10, 20, 30, 40])
ind=["A", "B", "C", "D"]
S=pd.Series(arr,index=ind)
print(S)
print(type(arr), type(S))