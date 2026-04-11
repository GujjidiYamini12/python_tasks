"""5. Accessing Matrix Data
A teacher stores marks of students in two subjects:
[[78, 85],
[90, 88],
[67, 72]]
Task:
● Convert it to a NumPy array.
● Access the second student's second subject mark"""
import numpy as np
lst=[]
for i in range(3):
    a,b=int(input()),int(input())
    lst.append([a,b])
arr=np.array(lst)
print(arr)
print(f"Second student's second subject mark: {arr[1,1]}")