"""9. Multi-Department Data Aggregation
A company collects employee counts from two branches.
Branch A:
[[10, 20],
[30, 40]]
Branch B:
[[5, 15],
[25, 35]]
Scenario:
● Combine the two matrices.
● Calculate the total employees across all departments.
● Print the combined matrix and total.
"""
import numpy as np
ar1=np.array([[10, 20], [30, 40]])
ar2=np.array([[5, 15], [25, 35]])
arr=np.concatenate((ar1,ar2))
sum_of_matrix=arr.sum()
print(f"Combined array: {arr} with sum of combined matrix: {sum_of_matrix}")