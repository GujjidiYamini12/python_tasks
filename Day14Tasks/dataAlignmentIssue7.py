"""7. Data Alignment Issue in Series Addition
Two Series:
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
Task:
● Add both Series
● Explain why some values become NaN
● Replace NaN with 0 and compute final result
"""
import pandas as pd
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
S3=S1+S2
print(S3)
"""Aligns by index labels, not by position. If a label is missing in either Series then result becomes NaN ex: a is NaN"""
S3=S3.fillna(0)
print(S3)