"""6. Multi-Line Graph for Sales Comparison
Scenario:
data = {
"Month": ["Jan", "Feb", "Mar"],
"Store_A": [100, 150, 200],
"Store_B": [90, 140, 210]
}
Task:
● Create DataFrame
● Plot two line graphs on same plot
● Add legend
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
data = {"Month": ["Jan", "Feb", "Mar"],"Store_A": [100, 150, 200],"Store_B": [90, 140, 210]}
df=pd.DataFrame(data)
plt.plot(data["Month"],data["Store_A"],label="Store_A",marker="o",color="green")
plt.plot(data["Month"],data["Store_B"],label="Store_B",marker="o",color="blue")
plt.title("Multi-Line Graph for Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()