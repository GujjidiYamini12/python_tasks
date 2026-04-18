"""2. Student Marks Bar Chart
Scenario:
Marks of students:
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])
Task:
● Create a DataFrame
● Plot a bar graph
● Show student names on X-axis"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])
df=pd.DataFrame(marks,index=names)
#plt.barh(names,marks,color='brown') horizontal line
plt.bar(names,marks,color='brown') #vertical line
plt.title("BAR GRAPH")
plt.xlabel("NAMES")
plt.ylabel("MARKS")
plt.show()