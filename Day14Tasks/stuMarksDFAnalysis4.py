"""4. Student Marks DataFrame Analysis
A DataFrame:
data = pd.DataFrame({
"Name": ["A", "B", "C"],
"Math": [80, 70, 60],
"Science": [90, 60, 70]
})
Task:
● Add a new column Total = Math + Science
● Find the student with the highest total marks"""
import pandas as pd
import numpy as np
data = pd.DataFrame({"Name": ["A", "B", "C"],"Math": [80, 70, 60],"Science": [90, 60, 70]})
data["Total"]=data["Math"]+data["Science"]
highest_tot_marks=data["Total"].idxmax()
print(data.loc[highest_tot_marks])