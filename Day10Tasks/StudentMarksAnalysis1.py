"""1. Student Marks Analysis
A teacher stores the marks of 5 students in a NumPy array.
Scenario:
You are given marks [45, 67, 89, 56, 72].
Task:
● Convert the list into a NumPy array.
● Add 5 grace marks to every student.
● Print the updated marks.
"""
import numpy as np
lst=[45, 67, 89, 56, 72]
arr=np.array(lst) #t1-list into a NumPy array
print(type(arr))
arr=arr+5 #t2-Add 5 grace marks
print(arr) #t3-Print the updated marks
