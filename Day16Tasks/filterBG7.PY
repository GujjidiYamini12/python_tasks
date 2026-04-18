"""7. Filtered Bar Chart
Scenario:
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]
Task:
● Convert to DataFrame
● Filter students with marks > 50
● Plot bar chart only for filtered students"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]
df=pd.DataFrame({"Names":names,"Marks":marks})
df1=df[df["Marks"]>50]
plt.bar(df1["Names"],df1["Marks"])
plt.xlabel("Names")
plt.ylabel("Marks")
plt.title("Filtered Bar Chart")
plt.show()