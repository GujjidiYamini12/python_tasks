"""5. Product Sales Bar Chart
Scenario:
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])
Task:
● Create DataFrame
● Plot bar chart
● Add labels and title
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])
df=pd.DataFrame(sales,index=products,columns=["sales"])
print(df)
plt.bar(df.index,df["sales"],color="red")
plt.xlabel("PRODUCTS")
plt.ylabel("SALES")
plt.title("Product Sales Bar Chart")
plt.show()