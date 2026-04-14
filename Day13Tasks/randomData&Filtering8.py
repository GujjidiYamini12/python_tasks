"""8. Random Data & Filtering
Generate random numbers:
nums = np.random.randint(1, 100, 10)
Task:
● Filter values that are divisible by 5
● Return sorted result."""
import numpy as np
import random
nums = np.random.randint(1, 100, 10)
fil_arr=nums%5==0
upd_arr=nums[fil_arr]
upd_arr.sort()
print(upd_arr)