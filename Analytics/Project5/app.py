# ============================================================
# 📊 Project Title: Car Data Analysis
# Analyze Car dataset using NumPy, Pandas, Matplotlib
# ============================================================

# ============================================================
# 📦 1. Import Required Libraries
# ============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# �� Scenario 1: Data Loading & Basic Cleaning
# ============================================================
# Understand the dataset structure and prepare it for analysis.
# �� Tasks:
# ● Load the dataset using Pandas.
df=pd.read_csv("cardata.csv")
# ● Display:
# ○ First 5 rows
print("-------------------------------------------------------------")
print(df.head())
print("-------------------------------------------------------------")
# ○ Last 5 rows
print("\n-------------------------------------------------------------")
print(df.tail())
print("-------------------------------------------------------------")
# ○ Column names
print("\n-------------------------------------------------------------")
print(df.columns)
print("-------------------------------------------------------------")
# ○ Shape of dataset
print(df.shape)
# ● Check data types of all columns.
print(df.dtypes)
# ● Check for missing values in:
# ○ Selling_Price
# ○ Present_Price
# ○ Kms_Driven
# ○ Fuel_Type
print(df[["Selling_Price","Present_Price","Kms_Driven","Fuel_Type"]].isnull().sum())
# ● Fill missing values:
# ○ Selling_Price → mean
# ○ Present_Price → mean
# ○ Kms_Driven → mean
# ○ Fuel_Type → mode
df["Selling_Price"]=df["Selling_Price"].fillna(df["Selling_Price"].mean(),inplace=True)
df["Present_Price"]=df["Present_Price"].fillna(df["Present_Price"].mean(),inplace=True)
df["Kms_Driven"]=df["Kms_Driven"].fillna(df["Kms_Driven"].mean(),inplace=True)
df["Fuel_Type"]=df["Fuel_Type"].fillna(df["Fuel_Type"].mode()[0],inplace=True)
# ● Convert numeric columns to proper numeric type if required:
# ○ Selling_Price
# ○ Present_Price
# ○ Kms_Driven
# ○ Year
df["Selling_Price"]=pd.to_numeric(df["Selling_Price"], errors="coerce")
df["Present_Price"]=pd.to_numeric(df["Present_Price"], errors="coerce")
df["Kms_Driven"]=pd.to_numeric(df["Kms_Driven"], errors="coerce")
df["Year"]=pd.to_numeric(df["Year"], errors="coerce")
# ● Convert Selling_Price and Kms_Driven into NumPy arrays.
# ● Use NumPy to calculate:
# ○ minimum selling price
# ○ maximum selling price
# ○ average selling price
Selling_Price_arr=df["Selling_Price"].to_numpy()
Kms_Driven_arr=df["Kms_Driven"].to_numpy()
min_selling_price=Selling_Price_arr.min()
max_selling_price=Selling_Price_arr.max()
avg_selling_price=Selling_Price_arr.mean()

# ============================================================
# �� Scenario 2: Selling Price Trend (Line Graph)
# ============================================================
# See how selling prices vary for a small sample of cars.
# �� Tasks:
# ● Select:
# ○ Car_Name
# ○ Selling_Price
select_df=df[["Car_Name","Selling_Price"]]
# ● Take the first 10 rows only using Pandas.
select_df=select_df.head(10)
# ● Convert Selling_Price into a NumPy array.
arr_Sp=select_df["Selling_Price"].to_numpy()
# ● Plot a line graph using Matplotlib:
# ○ X-axis → row index (0–9)
# ○ Y-axis → Selling Price
# ● Add:
# ○ title
# ○ x-axis label
# ○ y-axis label
# ○ markers
# ● Save the graph with a suitable filename.
plt.figure(figsize=(6,6))
plt.plot(select_df.index,arr_Sp,marker="o")
plt.xlabel("row index")
plt.ylabel("Selling Price")
plt.title("Selling Price Trend")
plt.tight_layout()
plt.savefig("Graphs/selling_price_trend.png")
plt.show()