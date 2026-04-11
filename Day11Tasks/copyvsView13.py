"""13. Copy vs View Behavior in Data Processing
Scenario:
A dataset:
[10, 20, 30, 40]
Task:
● Create a copy of the array.
● Modify the original array.
● Show that the copy does not change.
● Repeat using view() and observe the difference."""
import numpy as np
lst=[]
for i in range(4):
    lst.append(int(input()))
arr=np.array(lst)
print("Array: ",arr)
copy_arr=arr.copy()
print("Copied array: ",copy_arr)
arr[1]=50
print("Array after modification: ",arr)
print("Copied array after modification: ",copy_arr)
view_arr=arr.view()
print("viewed arr: ", view_arr)
arr[3]=60
print("Array after modification: ",arr)
print("View array after modification: ",view_arr)
