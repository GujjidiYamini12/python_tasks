"""11. Boolean Masking for Salary Analysis
Scenario:
Employee salaries:
[25000, 40000, 15000, 50000, 30000]
Task:
● Filter salaries above 30000.
● Count how many employees satisfy this condition."""
import numpy as np
lst=[]
for i in range(5):
    lst.append(int(input()))
arr=np.array(lst)
fil_arr=arr>30000
upd_arr=arr[fil_arr]
print(len(upd_arr))