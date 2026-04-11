"""11. Filter High Temperature Values
A weather station records temperatures:
[28, 31, 35, 27, 40, 22]
Scenario:
The system needs temperatures above 30°C.
Task:
● Filter the values greater than 30 using NumPy boolean filtering.
"""
import numpy as np
lst=[]
for i in range(6):
    lst.append(int(input()))
arr=np.array(lst)
print(arr)
ind=int(input())
filter_arr=arr>ind
new_arr=arr[filter_arr]
print(new_arr)