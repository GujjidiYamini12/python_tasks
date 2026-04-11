"""15. Reshape and Flatten Image Data
Scenario:
An image is stored as a 2 × 3 matrix:
[[1,2,3],
[4,5,6]]
Task:
1. Convert it into a NumPy array.
2. Flatten the array into 1-D format.
3. Print the flattened array"""
import numpy as np
lst=[]
for i in range(2):
    a,b,c=int(input()),int(input()),int(input())
    lst.append([a,b,c])
arr=np.array(lst)
print("Array: ",arr)
dim=int(input())
new_arr=arr.flatten()
print(f"Array shaped into {dim} dimensional array: {new_arr}")