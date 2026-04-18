"""9. Combined Visualization Dashboard
Scenario:
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]
Task:
● Create DataFrame
● Plot:
○ Line graph (trend)
○ Bar chart (comparison)
○ Pie chart (distribution)
● Show all in single figure (subplots)
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]
df=pd.DataFrame({"Pro":products,"sales":sales})
fig,ax=plt.subplots(1,3)
#Line Graph
ax[0].plot(df["Pro"],df["sales"],marker="o")
ax[0].set_title("Line graph (trend)")
ax[0].set_xlabel("Products")
ax[0].set_ylabel("Sales")
#Bar Graph
ax[1].bar(df["Pro"],df["sales"])
ax[1].set_title("Bar chart (comparison)")
ax[1].set_xlabel("Products")
ax[1].set_ylabel("Sales")
#Pie chart
ax[2].pie(df["sales"],labels=products,explode=(0,0,0,0),autopct="%1.1f%%")
ax[2].set_title("Pie chart (distribution)")
plt.show()