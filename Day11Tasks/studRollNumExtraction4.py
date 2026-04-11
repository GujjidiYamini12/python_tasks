""". Student Roll Numbers Extraction
A list contains roll numbers:
[101, 102, 103, 104, 105, 106]
Scenario:
You want only the middle students (index 2 to 4).
Task:
● Use NumPy slicing to extract those values.
"""
import numpy as np
lst=[]
for i in range(6):
    lst.append(int(input()))
arr=np.array(lst)
print("Array: ",arr)
print("Array Sliced: ",arr[2:5])