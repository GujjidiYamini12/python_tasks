"""6. Data Analysis Tool (NumPy + Pandas)
Scenario:
Analyze student marks.
Task:
● Generate marks using NumPy
● Convert into Pandas DataFrame
● Use conditions to filter passing students
● Calculate mean using math/NumPy
● Use loop to print results"""
import numpy as np
import pandas as pd
lst=np.random.randint(10,100,size=(5))
df=pd.DataFrame({"marks":lst})
print(df)
fil_df=df[df["marks"]>50]
print(fil_df)
fil_df_mean=np.mean(df["marks"])
print(fil_df_mean)
for i,mark in enumerate(df["marks"],start=0):
    status="pass" if mark>50 else "fail"
    print(i,mark,status)