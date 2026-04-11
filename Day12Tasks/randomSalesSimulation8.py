"""8. Random Sales Simulation
Scenario:
A company wants to simulate 10 days of sales (range 100–500).
Task:
● Generate random integers using NumPy.
● Print the array.
● Find the average sales.
"""
from numpy import random
no_of_days=int(input())
arr=random.randint(100,500,size=no_of_days)
print(arr)
avg=arr.sum()/no_of_days
print(avg)