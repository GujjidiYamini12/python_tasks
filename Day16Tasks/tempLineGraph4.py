"""4. Temperature Trend Line Plot
Scenario:
Daily temperatures:
temps = np.array([28, 30, 32, 31, 29])
Task:
● Convert into Pandas Series
● Plot a line graph
● Add title and grid
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
temps = np.array([28, 30, 32, 31, 29])
s=pd.Series(temps)
plt.plot(s,marker="o")
plt.title("TEMP TREND LINE PLOT")
plt.xlabel("Days")
plt.ylabel("Temp")
plt.grid()
plt.show()