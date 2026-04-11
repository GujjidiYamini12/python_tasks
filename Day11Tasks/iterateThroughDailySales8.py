"""8. Iterate Through Daily Sales
Daily sales data:
[200, 300, 150, 400]
Task:
● Store it in a NumPy array.
● Iterate through the array and print each sale value.
"""
import numpy as np
lst=[]
for i in range(4):
    lst.append(int(input()))
arr=np.array(lst)
print(arr)
for i in arr:
    print(i)

