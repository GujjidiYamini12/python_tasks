"""3. Add Constant to Series (NumPy Operation on Pandas)
A Series:
S = pd.Series([5, 10, 15])
Task:
● Add 5 to each element using NumPy-style operation
● Print updated Series
"""
import numpy as np
import pandas as pd
S = pd.Series([5, 10, 15])
print(S)
S=S+5
print(S)