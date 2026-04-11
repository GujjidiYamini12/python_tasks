"""6. Check Data Type of Inventory Values
A warehouse stores product quantities:
[10, 20, 30, 40]
Task:
● Convert it into a NumPy array.
● Print the data type (dtype) of the array.
"""
import numpy as np
lst=[]
for i in range(4):
    lst.append(int(input()))
arr=np.array(lst)
print("Data Type of array: ",arr.dtype)