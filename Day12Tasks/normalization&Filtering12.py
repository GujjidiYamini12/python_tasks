"""12. Random Dataset Normalization + Filtering
Scenario:
● Generate 8 random float values between 0 and 1.
Task:
1. Normalize by multiplying with 100
2. Filter values greater than 50
3. Sort the filtered values"""
from numpy import random
arr=random.rand(8)
arr=arr*100
fil_arr=arr>50
upd_arr=arr[fil_arr]
upd_arr.sort()
print(upd_arr)