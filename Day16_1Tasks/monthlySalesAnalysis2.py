"""2. Monthly Sales Analysis
Scenario:
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → month-wise comparison
○ Pie chart → contribution of each month
○ Histogram → frequency of sales values
○ Scatter plot → month index vs sales"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df=pd.DataFrame({"months":months,"sales":sales})
fig,ax=plt.subplots(2,3)
ax[0][0].plot(df["months"],df["sales"])
ax[0][0].set_title("Line graph → sales trend")
ax[0][0].set_xlabel("months")
ax[0][0].set_ylabel("sales")

ax[0][1].bar(df["months"],df["sales"])
ax[0][1].set_title("Bar chart → month-wise comparison")
ax[0][1].set_xlabel("months")
ax[0][1].set_ylabel("sales")


ax[0][2].pie(df["sales"],labels=df["months"],explode=(0.1,0,0,0,0,0),autopct="%1.1f%%")
ax[0][2].set_title("Pie chart → contribution of each month")

ax[1][0].hist(df["sales"],10)
ax[1][0].set_title("Histogram → frequency of sales values")
ax[1][0].set_xlabel("sales")
ax[1][0].set_ylabel("Frequency")

ax[1][1].scatter(df.index,df["sales"])
ax[1][1].set_title("Scatter plot → month index vs sales")
ax[1][1].set_xlabel("Index")
ax[1][1].set_ylabel("sales")
fig.delaxes(ax[1][2])
plt.tight_layout()
plt.show()