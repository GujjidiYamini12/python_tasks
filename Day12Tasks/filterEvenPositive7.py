"""7. Filter Positive Even Numbers from Dataset
Scenario:
A dataset contains mixed values:
arr = [-5, 10, 15, -2, 20, 25, 30]
Task:
● Convert to NumPy array.
● Filter values that are:
○ Positive
○ Even"""
import numpy as np
arr=[]
for i in range(7):
    arr.append(int(input()))
new_arr=np.array(arr)
fil_arr=[]
for i in new_arr:
    if i>0 and i%2==0:
        fil_arr.append(True)
    else:
        fil_arr.append(False)
con_new_arr=new_arr[fil_arr]
print(new_arr,"\n",fil_arr,"\n",con_new_arr)