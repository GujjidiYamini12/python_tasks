"""6. Student Marks Analysis (NumPy → Pandas)
Marks data:
arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])
Task:
● Convert into DataFrame with columns "Math", "Science"
● Add a new column Total
● Find student with highest total
"""
import numpy as np
import pandas as pd
arr = np.array([[80, 90],[70, 60],[85, 95]])
df=pd.DataFrame(arr,columns=["Math", "Science"])
print(df)
df["Total"]=df["Math"]+df["Science"]
print(df)
print(df.loc[df["Total"].idxmax()])