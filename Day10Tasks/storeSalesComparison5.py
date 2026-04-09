"""5. Store Sales Comparison
Two stores record daily sales for 3 days.
Scenario:
Store A = [200, 250, 300]
Store B = [180, 270, 310]
Task:
● Store them in NumPy arrays.
● Find the daily difference in sales between the two stores.
● Print the resulting array.
"""
import math as m
import numpy as np
A = [200, 250, 300]
B = [180, 270, 310]
ar1=np.array(A)
ar2=np.array(B)
ar3=np.abs(ar1-ar2)
print(ar3)