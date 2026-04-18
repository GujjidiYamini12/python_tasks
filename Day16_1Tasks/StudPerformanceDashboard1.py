""". Student Performance Dashboard
Scenario:
A school records marks of students in one subject:
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
Task:
● Convert to Pandas DataFrame
● Plot:
○ Line graph → trend of marks
○ Bar chart → student vs marks
○ Pie chart → Pass (>50) vs Fail
○ Histogram → distribution of marks
○ Scatter plot → index vs marks
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
df=pd.DataFrame({"Stud":students,"Marks":marks})
fig,ax=plt.subplots(2,3)
ax[0][0].plot(df["Stud"],df["Marks"])
ax[0][0].set_title("Line graph → trend of marks")
ax[0][0].set_xlabel("STUDENTS")
ax[0][0].set_ylabel("MARKS")

ax[0][1].bar(df["Stud"],df["Marks"])
ax[0][1].set_title("Bar chart → student vs marks")
ax[0][1].set_xlabel("STUDENTS")
ax[0][1].set_ylabel("MARKS")

Pass=df[df["Marks"]>50]
c_p=len(Pass)
Fail=df[df["Marks"]<=50]
c_f=len(Fail)
count=[c_p,c_f]
ax[0][2].pie(count,labels=["Pass","Fail"],explode=(0.1,0),autopct="%1.1f%%")
ax[0][2].set_title("Pie chart → Pass (>50) vs Fail")

ax[1][0].hist(df["Marks"],10)
ax[1][0].set_title("Histogram → distribution of marks")
ax[1][0].set_xlabel("Marks")
ax[1][0].set_ylabel("Frequency")

ax[1][1].scatter(df.index,df["Marks"])
ax[1][1].set_title("index vs marks")
ax[1][1].set_xlabel("Index")
ax[1][1].set_ylabel("MARKS")
fig.delaxes(ax[1][2])
plt.tight_layout()
plt.show()