"""10. Data Processing Pipeline
A data pipeline receives the following array:
[12, 7, 25, 3, 18, 10]
Scenario:
1. Convert the list into a NumPy array.
2. Sort the array.
3. Split the sorted array into two equal parts.
4. Calculate the sum of each part.
Output:
● Sorted array
● Two split arrays
● Sum of each part"""
import numpy as np
data = [12, 7, 25, 3, 18, 10]
ar1=np.array(data)
sorted_arr=np.sort(ar1)
arr_split=np.array_split(sorted_arr,2)
print(f"Given data: {data}\nConverted array: {ar1}\nSorted array: {sorted_arr}\narray split: {arr_split}")
for i in arr_split:
    print(f"{i} sum is {i.sum()}")