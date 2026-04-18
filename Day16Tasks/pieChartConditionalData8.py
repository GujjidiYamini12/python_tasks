"""8. Pie Chart with Conditional Data
Scenario:
scores = np.array([40, 60, 80, 30, 90])
Task:
● Categorize into:
○ Pass (>50)
○ Fail (<=50)
● Count using NumPy/Pandas
● Plot pie chart for Pass vs Fail"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
scores = np.array([40, 60, 80, 30, 90])
Pass=scores[scores>50]
count_p=len(Pass)
Fail=scores[scores<=50]
count_f=len(Fail)
count=[count_p,count_f]
plt.pie(count,labels=["Pass","Fail"],explode=(0.1,0),autopct="%1.1f%%",shadow=True,startangle=90)
plt.title("Pie Chart with Conditional Data")
plt.show()
