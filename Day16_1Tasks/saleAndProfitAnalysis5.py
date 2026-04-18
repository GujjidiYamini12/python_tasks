"""5. Product Sales & Profit Analysis
Scenario:
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → product vs sales
○ Pie chart → sales contribution
○ Histogram → profit distribution
○ Scatter plot → sales vs profit"""
import numpy as np,pandas as pd
from matplotlib import pyplot as plt
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
df=pd.DataFrame({"sales":sales,"profit":profit,"products":products})
fig,ax=plt.subplots(2,3)
ax[0][0].plot(df.index,df["sales"],marker="o")
ax[0][0].set_title("Line graph → sales trend")
ax[0][0].set_xlabel("Index")
ax[0][0].set_ylabel("Sales")

ax[0][1].bar(df["products"],df["sales"])
ax[0][1].set_title("Bar chart → product vs sales")
ax[0][1].set_xlabel("products")
ax[0][1].set_ylabel("sales")

ax[0][2].pie(df["sales"],labels=df["products"],explode=(0.1,0,0,0,0),autopct="%1.1f%%",startangle=90)
ax[0][2].set_title("Pie chart → sales contribution")

ax[1][0].hist(df["profit"],bins=5)
ax[1][0].set_title("Histogram → profit distribution")
ax[1][0].set_xlabel("profit")
ax[1][0].set_ylabel("Frrequecy")

ax[1][1].scatter(df["sales"],df["profit"])
ax[1][1].set_title("Scatter plot → sales vs profit")
ax[1][1].set_xlabel("sales")
ax[1][1].set_ylabel("profit")
fig.delaxes(ax[1][2])
plt.tight_layout()
plt.show()