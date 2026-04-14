"""5. Reshape & Row Averages
A dataset:
data = np.arange(1, 13)
Task:
● Reshape it into a 3×4 matrix
● Compute average of each row"""
import numpy as np
import random
data = np.arange(1, 13)
print(data)
row=int(input())
col=int(input())
re_data=data.reshape(row, col)
print(re_data)
avg_of_row=np.mean(re_data,axis=1)
print(avg_of_row)