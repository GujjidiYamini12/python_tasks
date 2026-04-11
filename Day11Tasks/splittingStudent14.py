"""14. Splitting Student Scores Across Servers
A dataset:
[50, 60, 70, 80, 90, 100, 110, 120]
Scenario:
A distributed system needs to divide this data among 4 servers.
Task:
● Convert to NumPy array.
● Split the array into 4 equal parts using array_split()."""
import numpy as np
lst=[]
for i in range(8):
    lst.append(int(input()))
arr=np.array(lst)
print("Array: ",arr)
ind=int(input())
new_arr=np.array_split(arr,ind)
print("Array splitted: ",new_arr)