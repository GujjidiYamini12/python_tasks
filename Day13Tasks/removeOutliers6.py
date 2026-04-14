"""6. Remove Outliers
Given data:
values = np.array([10, 12, 15, 18, 100, 14, 13])
Task:
● Compute the mean and standard deviation
● Remove values that are more than 2 standard deviations from the mean"""
import numpy as np
values = np.array([10, 12, 15, 18, 100, 14, 13])
mean=np.mean(values)
sd=np.std(values)
fil_arr=np.fabs(values-mean)<=2*sd
upd_arr=values[fil_arr]
print(upd_arr)
