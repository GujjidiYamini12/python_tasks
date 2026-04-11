"""3. Product Rating System
An e-commerce website stores product ratings:
[4, 5, 3, 4, 2]
Task:
● Convert it to a NumPy array.
● Print the first and last rating using indexing."""
import numpy as np
lst=[]
for i in range(5):
    lst.append(int(input()))
arr=np.array(lst)
print(arr)
print(f"first element: {arr[0]}\nLast element: {arr[-1]}")