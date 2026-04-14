"""6. Row Selection & Deletion
A DataFrame:
df = pd.DataFrame({
"A": [10, 20, 30],
"B": [5, 15, 25]
}, index=["x", "y", "z"])
Task:
● Select row with index "y"
● Delete row "x"
● Print updated DataFrame"""
import pandas as pd
df = pd.DataFrame({"A": [10, 20, 30],"B": [5, 15, 25]}, index=["x", "y", "z"])
print(df.loc["y"])
df=df.drop("x") #drop() is a function it is used to delete row 
#Rows = indexed records → must use drop()
print(df)