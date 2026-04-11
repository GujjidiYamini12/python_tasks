""". Bank Transaction Storage
A bank stores the transaction amounts of a customer in a list:
[1200, 500, 800, 1500]
Scenario:
● Convert the list into a NumPy array.
● Print the type of the object.
● Verify that it is a NumPy ndarray"""
import numpy as np
lst=[]
for i in range(4):
    lst.append(int(input()))
arr=np.array(lst)
print(type(arr))

print(True) if type(arr)==np.ndarray else print(False)