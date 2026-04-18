"""10. Data Cleaning + Visualization
Scenario:
data = np.array([100, np.nan, 200, 150, np.nan, 300])
Task:
1. Convert to Pandas Series
2. Replace NaN with mean
3. Plot:
○ Line graph of cleaned data
○ Bar chart of values > average"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
data = np.array([100, np.nan, 200, 150, np.nan, 300])
s=pd.Series(data)
avg=s.mean()
s=s.fillna(avg)
fig,ax=plt.subplots(2,1)
ax[0].plot(s,marker="o")
ax[0].set_title("Line graph of cleaned data")
ax[0].set_xlabel("Index")
ax[0].set_ylabel("Data")
more_avg=s[s>avg]
ax[1].bar(more_avg.index,more_avg.values)
ax[1].set_title("Bar chart of values > average")
ax[1].set_xlabel("Index")
ax[1].set_ylabel("Data")
plt.show()