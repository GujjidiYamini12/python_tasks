"""6. Multi-Level List Transformation (Advanced List Comprehension)
A dataset contains:
data = [[1, 2, 3], [4, 5], [6]]
Task:
● Flatten the list using list comprehension.
● Then create a new list containing squares of only even numbers.
"""
import numpy as np
data = [[1, 2, 3], [4, 5], [6]]
lst=[j for i in data for j in i]
print(lst)
even_lst=[i**2 for i in lst if i%2==0]
print(even_lst)