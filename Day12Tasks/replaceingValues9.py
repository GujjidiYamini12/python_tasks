"""9. Replace Values Using Filtering
Scenario:
A dataset contains:
[5, 12, 18, 7, 25, 30]
Task:
● Replace all values greater than 15 with 0 using NumPy filtering."""
import numpy as np
arr=[]
for i in range(6):
    arr.append(int(input()))
new_arr=np.array(arr)
new_arr[new_arr>15]=0
print(new_arr)