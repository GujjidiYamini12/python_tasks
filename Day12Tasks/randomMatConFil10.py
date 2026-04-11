"""10. Random Matrix and Condition Filtering
Scenario:
● Generate a 3×3 matrix of random numbers (0–50).
Task:
● Filter elements greater than 25.
● Print filtered values."""
from numpy import random
arr=random.randint(50,size=(3,3))
fil_arr=arr>25
upd_arr=arr[fil_arr]
print(arr)
print(fil_arr)
print(upd_arr)