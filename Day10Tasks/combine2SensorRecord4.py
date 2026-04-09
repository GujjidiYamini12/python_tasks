"""4. Combine Two Sensor Readings
Two sensors record readings during a test.
Scenario:
Sensor1 = [10, 20, 30]
Sensor2 = [40, 50, 60]
Task:
● Store both readings in NumPy arrays.
● Combine them into one array using NumPy concatenation.
"""
import numpy as np
Sensor1 = [10, 20, 30]
Sensor2 = [40, 50, 60]
ar1=np.array(Sensor1)
ar2=np.array(Sensor2)
arr=np.concatenate((ar1,ar2))
print(arr)