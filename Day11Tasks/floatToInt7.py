"""7. Convert Float Prices to Integer
A shop stores product prices:
[10.5, 20.8, 15.3]
Scenario:
The billing system requires integer values.
Task:
● Convert the array from float to integer using astype()."""
import numpy as np
lst=[]
for i in range(3):
    lst.append(float(input()))
arr=np.array(lst)
newarr=arr.astype('i')
print(arr)
print(newarr)