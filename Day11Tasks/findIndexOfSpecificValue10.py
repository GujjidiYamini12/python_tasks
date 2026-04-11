"""10. Find Indexes of Specific Value
A quality check system stores product defect codes:
[2, 4, 1, 4, 3, 4, 5]
Task:
● Find the indexes where value = 4 using NumPy searching"""
import numpy as np
lst=[]
for i in range(7):
    lst.append(int(input()))
arr=np.array(lst)
print(arr)
ind=int(input())
val=np.where(arr==ind)
print(val)