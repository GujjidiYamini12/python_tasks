"""8. Complex DataFrame Transformation
A DataFrame:
df = pd.DataFrame({
"Name": ["A", "B", "C", "D"],
"Marks": [50, 80, 30, 90]
})
Scenario:
● Students scoring below 50 failed
Task:
1. Create a column Status ("Pass"/"Fail")
2. Filter only passed students
3. Calculate average marks of passed students"""
import pandas as pd
import numpy as np
df = pd.DataFrame({"Name": ["A", "B", "C", "D"],"Marks": [50, 80, 30, 90]})
print(df)
df["Status"]=["Pass" if i>=50 else "Fail" for i in df["Marks"]]
print(df)
fil_df=df[df["Status"]=="Pass"]
print(fil_df)
mean_of_pass=np.mean(fil_df["Marks"])
print(mean_of_pass)