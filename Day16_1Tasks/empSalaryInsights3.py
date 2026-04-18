"""3. Employee Salary Insights
Scenario:
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
Task:
● Convert into DataFrame
● Plot:
○ Line graph → salary trend
○ Bar chart → department-wise salary comparison
○ Pie chart → department distribution
○ Histogram → salary distribution
○ Scatter plot → index vs salary
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
df=pd.DataFrame({"salaries":salaries,"departments":departments})
fig,ax=plt.subplots(2,3)
ax[0][0].plot(df.index,df["salaries"])
ax[0][0].set_title("Line graph → salary trend")
ax[0][0].set_xlabel("Index")
ax[0][0].set_ylabel("salaries")

avg_of_dept=df.groupby("departments")["salaries"].mean()
ax[0][1].bar(avg_of_dept.index,avg_of_dept.values)
ax[0][1].set_title("Bar chart → department-wise salary comparison")
ax[0][1].set_xlabel("departments")
ax[0][1].set_ylabel("salaries")

dp_count=df["departments"].value_counts()
ax[0][2].pie(dp_count.values,labels=dp_count.index,explode=(0.1,0,0),autopct="%1.1f%%")
ax[0][2].set_title("Pie chart → department distribution")

ax[1][0].hist(df["salaries"],5)
ax[1][0].set_title("Histogram → salary distribution")
ax[1][0].set_xlabel("salaries")
ax[1][0].set_ylabel("Frequency")

ax[1][1].scatter(df.index,df["salaries"])
ax[1][1].set_title("Scatter plot → index vs salary")
ax[1][1].set_xlabel("Index")
ax[1][1].set_ylabel("salary")
fig.delaxes(ax[1][2])
plt.tight_layout()
plt.show()