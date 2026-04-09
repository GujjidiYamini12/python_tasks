"""3. Sorting Product Prices
An e-commerce company stores product prices in a NumPy array.
Scenario:
Prices = [499, 299, 799, 199, 599]
Task:
● Convert it into a NumPy array.
● Sort the prices in ascending order.
"""
import numpy as np
Prices = [499, 299, 799, 199, 599]
arr=np.array(Prices)
print(np.sort(arr)) #sort is numpy f'n not array f'n
