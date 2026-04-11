"""2. Device Sensor Value (Scalar Array)
An IoT device records a single sensor reading = 75.
Task:
● Create a 0-D NumPy array with this value.
● Print the value and check its number of dimensions.
"""
import numpy as np
sensor=int(input())
arr=np.array(sensor)
print(f"array: {arr} with dimensions: {arr.ndim}")