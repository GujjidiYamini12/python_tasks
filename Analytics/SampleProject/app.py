"""==========================================================================================
�� Scenario 1: Basic Data Loading & Cleaning
=============================================================================================
You are given a CSV file containing railway gauge data.
�� Tasks:
1. Load the dataset into a Pandas DataFrame.
2. Display the first 5 rows and column names.
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("railway_gauges 1.csv")
print(df.head())
print(df.iloc[[df["Total"].idxmax()]])
"""===========================================================================================
�� Scenario 2: Simple Visualization
=============================================================================================
You want a quick understanding of total railway track growth.
�� Tasks:
1. Extract Year and Total columns.
2. Plot a bar graph showing Number of railway tracks installed per year.
3. Add:
○ Title
○ X and Y labels
4. Identify whether the trend is increasing or decreasing"""
df=df.drop("Total",axis=1)
ax=df.plot(x="Year",kind="bar")
plt.xticks(rotation=70)
plt.xlabel("YEAR")
plt.ylabel("TOTAL")
plt.title("Gauges: Number of railway tracks installed per year")
plt.savefig("rail_gauges.png")
plt.show()