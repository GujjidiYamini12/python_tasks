"""3. Expense Distribution Pie Chart
Scenario:
Monthly expenses:
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
Task:
● Create a pie chart
● Show percentage distribution"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
explode=(0.1,0.1,0.1)
fig1,ax1=plt.subplots()
ax1.pie(expenses,labels=labels, autopct="%1.1f%%",startangle=270,explode=explode,shadow=True)
ax1.axis("equal")
plt.show()
