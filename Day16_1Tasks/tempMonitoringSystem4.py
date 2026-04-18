"""4. Temperature Monitoring System
Scenario:
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → daily temperature trend
○ Bar chart → day-wise temperature
○ Pie chart → proportion of high (>30) vs low temps
○ Histogram → temperature frequency
○ Scatter plot → day index vs temperature
"""
import numpy as np,pandas as pd
from matplotlib import pyplot as plt
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
df=pd.DataFrame({"Day":days,"Temp":temps})
fig,ax=plt.subplots(2,3)
ax[0][0].plot(df["Day"],df["Temp"],marker="o")
ax[0][0].set_title("Line graph → daily temperature trend")
ax[0][0].set_xlabel("Days")
ax[0][0].set_ylabel("Temps")

ax[0][1].bar(df["Day"],df["Temp"])
ax[0][1].set_title("Bar chart → day-wise temperature")
ax[0][1].set_xlabel("Days")
ax[0][1].set_ylabel("Temps")

high_t=df[df["Temp"]>30]
c_ht=len(high_t)
low_t=df[df["Temp"]<=30]
c_lt=len(low_t)
pro_temp=[c_ht,c_lt]
ax[0][2].pie(pro_temp,labels=["High","Low"],explode=(0.1,0),autopct="%1.1f%%")
ax[0][2].set_title("Pie chart → proportion of high (>30) vs low temps")

ax[1][0].hist(df["Temp"],bins=5)
ax[1][0].set_title("Histogram → temperature frequency")
ax[1][0].set_xlabel("Temperature")
ax[1][0].set_ylabel("Frequency")

ax[1][1].scatter(df.index,df["Temp"])
ax[1][1].set_title("Scatter plot → day index vs temperature")
ax[1][1].set_xlabel("Index")
ax[1][1].set_ylabel("temperature")
fig.delaxes(ax[1][2])
plt.tight_layout()
plt.show()