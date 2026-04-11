"""12. Sorting Customer Names
A system stores customer names:
["Ravi", "Anil", "Sita", "John"]
Task:
● Convert it to a NumPy array.
● Sort the names alphabetically.
"""
import numpy as np
lst=[]
for i in range(4):
    lst.append(input())
arr=np.array(lst)
print("Array: ",arr)
print("Array Sorted: ",np.sort(arr))