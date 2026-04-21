# =======================================================================================================
# 📊 Project Title: Railway Gauge Data Analysis
# Analyze railway gauge dataset using NumPy, Pandas, Matplotlib
# =======================================================================================================

# ========================================================================================================
# 📦 1. Import Required Libraries
# ========================================================================================================

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# =========================================================================================================
# �� Scenario 1: Basic Data Loading & Cleaning
# =========================================================================================================
# You are given a CSV file containing railway gauge data.
# �� Tasks:
# 1. Load the dataset into a Pandas DataFrame.
# 2. Display the first 5 rows and column names.
# 3. Check for missing values and replace them with 0.
# 4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.

df=pd.read_csv("railway_gauges 1.csv")
print(df.head())
print(df.columns)
df=df.fillna(0)
print(df.dtypes)
for i in df.columns:
    if i!="Year":
        df[i]=pd.to_numeric(df[i],errors="coerce")
print(df.dtypes)

# ===========================================================================================================
# �� Scenario 2: Simple Visualization
# ===========================================================================================================
# You want a quick understanding of total railway track growth.
# �� Tasks:
# 1. Extract Year and Total columns.
# 2. Plot a line graph showing Total tracks over years.
# 3. Add:
# ○ Title
# ○ X and Y labels
# 4. Identify whether the trend is increasing or decreasing

Year=df["Year"]
total=df["Total"]
plt.plot(Year,total,marker="o")
plt.xlabel("YEAR")
plt.ylabel("TOTAL")
plt.title("Total tracks over years")
plt.tight_layout()
plt.show()
print("Trend is increasing year by year but with some dips in later years")

# ============================================================================================================
# �� Scenario 3: Filtering + Bar Chart
# ============================================================================================================
# You are asked to analyze modern railway expansion.
# �� Tasks:
# 1. Filter the dataset for years after 2000.
# 2. Select Broad Gauge, Metre Gauge, and Narrow Gauge.
# 3. Plot a grouped bar chart comparing all three gauges.
# 4. Add legend and proper labels.
# 5. Identify which gauge dominates in recent years.

df["Year_in_int"]=df["Year"].str[:4].astype(int)
fil_df=df[df["Year_in_int"]>2000]

select_bmn=fil_df[["Broad Gauge","Metre Gauge","Narrow Gauge"]]
x=np.arange(len(fil_df["Year_in_int"]))
plt.style.use("ggplot")

width=0.2
plt.bar(x-width,select_bmn["Broad Gauge"],align="center",label="Broad",color="grey")
plt.bar(x,select_bmn["Metre Gauge"],align="center",label="Metre",color="blue")
plt.bar(x+width,select_bmn["Narrow Gauge"],align="center",label="Narrow",color="green")
plt.ylabel("three gauges")
plt.xlabel("Year")
plt.title("bar chart comparing all three gauges")
plt.xticks(x,fil_df["Year_in_int"])
plt.legend()
plt.show()
print("Broad gauge dominented since 2000")

# ==========================================================================================
# �� Scenario 4: Feature Engineering + Pie Chart
# ==========================================================================================
# You want to analyze the contribution of each gauge type.
# �� Tasks:
# 1. Calculate total sum of each gauge across all years.
# 2. Create a new structure (Series/DataFrame) for totals.
# 3. Plot a pie chart showing percentage contribution.
# 4. Add percentage labels (autopct).
# 5. Interpret which gauge contributes the most.

s_total=pd.Series({"BGT":df["Broad Gauge"].sum(),
                      "MGT":df["Metre Gauge"].sum(),
                      "NGT":df["Narrow Gauge"].sum()})
#print(s_total)
plt.pie(s_total,labels=["Broad Gauge","Metre Gauge","Narrow Gauge"],
        autopct="%1.1f%%",explode=(0.1,0,0),startangle=180)
plt.title("percentage contribution")
plt.show()
print("Broad Gauge contributes the most to the total railway network among all gauge types.")

# ==========================================================================================
# �� Scenario 5: Advanced Analysis + Multiple Graphs
# =============================================================================================
# You are asked to perform a complete analysis of railway trends.
# �� Tasks:
# 1. Create new columns:
# ○ % Broad Gauge
# ○ % Metre Gauge
# ○ % Narrow Gauge
# 2. Use NumPy (np.diff) to calculate yearly growth of Total tracks.
# 3. Plot:
# ○ Line graph for all gauges
# ○ Stacked bar chart showing composition
# 4. Highlight:
# ○ Years with highest growth
# ○ Decline in any gauge
# 5. Provide a final conclusion:
# �� “Is the railway system shifting towards a single dominant gauge?”

df["% Broad Gauge"]=(df["Broad Gauge"]/df["Total"])*100
df["% Metre Gauge"]=(df["Metre Gauge"]/df["Total"])*100
df["% Narrow Gauge"]=(df["Narrow Gauge"]/df["Total"])*100
df["Yearly_growth"]=np.insert(np.diff(df["Total"]),0,0)
print(df["Yearly_growth"])
plt.plot(df["Year_in_int"],df["Narrow Gauge"],label="Narrow Gauge",marker="o",color="grey")
plt.plot(df["Year_in_int"],df["Metre Gauge"],label="Metre Gauge",marker="o",color="green")
plt.plot(df["Year_in_int"],df["Broad Gauge"],label="Broad Gauge",marker="o",color="blue")
plt.ylabel("Gauges")
plt.xlabel("Year")
plt.legend()
plt.show()
plt.bar(df["Year_in_int"],df["Narrow Gauge"],label="Narrow Gauge",color="grey")
plt.bar(df["Year_in_int"],df["Metre Gauge"],label="Metre Gauge",color="green",bottom=df["Narrow Gauge"])
plt.bar(df["Year_in_int"],df["Broad Gauge"],label="Broad Gauge",color="blue",bottom=df["Metre Gauge"]+df["Narrow Gauge"])
plt.ylabel("Gauges")
plt.xlabel("Year")
plt.legend()
plt.show()
year_highest_growth=df.loc[df["Yearly_growth"].idxmax(),"Year_in_int"]
print(year_highest_growth)
print("Decline years:")
print(df.loc[df["Yearly_growth"] < 0, "Year_in_int"])
print("Yes, the railway system is clearly shifting toward a single dominant gauge that is Broad Gauge.")