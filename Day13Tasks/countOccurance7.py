"""7. Count Occurrences
You have:
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
Task:
● Count how many times each unique number appears.
● Return numbers with their counts.
"""
import numpy as np
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
dit={}
data_set=set(data)
for i in data_set:
    count=0
    for j in data:
        if i==j:
            count+=1
    dit[i]=count
print(dit)