# ============================================================
# 📊 Project Title: Gaming Review Data Analysis
# Analyze ign.csv dataset using NumPy, Pandas, Matplotlib
# ============================================================


# ============================================================
# 📦 1. Import Required Libraries
# ============================================================

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# =====================================================================
# �� Scenario 1: Data Loading & Preprocessing
# =====================================================================
# You are given the ign.csv dataset containing game reviews.
# �� Tasks:
# 1. Load the dataset using Pandas.
# 2. Display:
# ○ First 5 rows (head())
# ○ Last 5 rows (tail())
# ○ Shape of dataset
# 3. Remove the unnecessary column:
# ○ "Unnamed: 0" (index column)
# 4. Check for missing values in:
# ○ score, genre, platform
# 5. Handle missing values:
# ○ Fill numeric column score with mean
# ○ Fill categorical column genre with mode
# 6. Ensure correct data types:
# ○ score → float
# ○ release_year, release_month, release_day → integer

df=pd.read_csv("ign.csv")
print(df.head())
print(df.tail())
print(df.shape)
df=df.drop(columns=["Unnamed: 0"],errors="ignore")
df[df[["score","genre","platform"]].isnull().any(axis=1)]
df["score"]=df["score"].fillna(df["score"].mean())
df["genre"]=df["genre"].fillna(df["genre"].mode()[0])

df["score"]=df["score"].astype(float)
df["release_year"]=df["release_year"].astype(int)
df["release_month"]=df["release_month"].astype(int)
df["release_day"]=df["release_day"].astype(int)


# =====================================================================
# �� Scenario 2: Line Graph (Score Trend) + Save
# =====================================================================
# You want to analyze how game scores change over time.
# �� Tasks:
# 1. Group data by release_year.
# 2. Calculate average score per year using Pandas.
# 3. Convert results into NumPy arrays.
# 4. Plot a line graph:
# ○ X-axis → release_year
# ○ Y-axis → average score
# 5. Add:
# ○ Title: "Average Game Score Over Years"
# ○ Axis labels
# 6. Save the graph: plt.savefig("avg_score_trend.png")

groupedData=df.groupby("release_year")
avg_score_per_year=groupedData["score"].mean()
year=avg_score_per_year.index.to_numpy()
arr_avg_score=avg_score_per_year.to_numpy()
#print(arr_avg_score)
plt.plot(year,arr_avg_score,marker="o")
plt.xlabel("Release Year")
plt.ylabel("Average score")
plt.title("Average Game Score Over Years")
plt.savefig("avg_score_trend.png")
plt.show()

# =====================================================================
# �� Scenario 3: Filtering + Bar Chart + Save
# =====================================================================
# You want to compare top platforms.
# �� Tasks:
# 1. Filter dataset where:
# ○ score > 7
# 2. Count number of high-rated games per platform.
# 3. Select top 10 platforms using Pandas.
# 4. Convert data into NumPy arrays.
# 5. Plot a bar chart:
# ○ X-axis → platform
# ○ Y-axis → count of games
# 6. Rotate x-axis labels for readability.
# Save the graph: plt.savefig("top_platforms_bar.png")

fill_df=df[df["score"]>7]
high_rated_games_platform=fill_df.groupby("platform").size()
highest10=high_rated_games_platform.sort_values(ascending=False).head(10)
platform=highest10.index.to_numpy()
count=highest10.values

plt.figure(figsize=(10,6))
plt.bar(platform,count)
plt.xlabel("platform")
plt.ylabel("count of games")
plt.title("TOP PLATFORMS")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig("top_platforms_bar.png")
plt.show()

# # =====================================================================
# �� Scenario 4: Aggregation + Pie Chart + Save
# # =====================================================================
# You want to analyze genre distribution.
# �� Tasks:
# 1. Count the number of games per genre.
# 2. Select top 5 genres using Pandas.
# 3. Prepare labels and values.
# 4. Plot a pie chart:
# ○ Labels → genre
# ○ Values → count
# 5. Add percentage labels (autopct).
# Save the graph: plt.savefig("genre_distribution.png")

no_of_games_genre=df.groupby("genre").size()
top_games_genre=no_of_games_genre.sort_values(ascending=False).head(5)
top_genre=top_games_genre.index
count=top_games_genre.values
plt.figure(figsize=(6,6))
plt.pie(count,labels=top_genre,autopct="%1.1f%%")
plt.title("Genre Distribution")
plt.tight_layout()
plt.savefig("genre_distribution.png")
plt.show()

# # =====================================================================
# �� Scenario 5: Advanced Analysis + Multiple Graphs
# # =====================================================================
# You are asked to perform a detailed analysis of review patterns.
# # =====================================================================
# � Part 1: Feature Engineering
# # =====================================================================
# 1. Create a new column:
# ○ score_category:
# ■ score >= 9 → "Excellent"
# ■ 7 <= score < 9 → "Good"
# ■ < 7 → "Average"
# 2. Convert editors_choice:
# ○ Y → 1, N → 0

# # =====================================================================
# �� Part 2: NumPy Analysis
# # =====================================================================
# 3. Use NumPy to:
# ○ Calculate yearly score growth using np.diff() on average yearly scores

# # =====================================================================
# �� Part 3: Visualizations
# # =====================================================================
# �� Line Graph

# # =====================================================================
# 4. Plot trend of:
# # =====================================================================
# ○ Average score per release_year

# # =====================================================================
# �� Part 4: Save All Graphs
# # =====================================================================
# plt.savefig("score_trend.png")
# plt.savefig("score_category_stacked.png")
# plt.savefig("score_distribution.png")

# # =====================================================================
# �� Stacked Bar Chart
# 5. Show count of:
# # =====================================================================
# ○ score_category per release_year
# �� Histogram
# 6. Plot distribution of:
# ○ score

df["score_category"]=["Excellent" if i>=9 else "Good" if i>=7 else "Average" for i in df["score"]]
df["editors_choice"]=np.where(df["editors_choice"]=="Y",1,0)
yearly_score_growth=np.insert(np.diff(arr_avg_score),0,0)

plt.plot(year,yearly_score_growth,marker="o")
plt.ylabel("Average Score Growth")
plt.xlabel("Release Year")
plt.title("Yearly Score Growth")
plt.tight_layout()
plt.savefig("score_trend.png")
plt.show()

score_cty=df.groupby(["release_year","score_category"]).size()
tab=score_cty.unstack(fill_value=0)
exc=np.array(tab["Excellent"])
avg=np.array(tab["Average"])
good=np.array(tab["Good"])
years = tab.index.to_numpy()
x = np.arange(len(years)) 

plt.figure(figsize=(10,6))
plt.bar(x,good,width=0.5,label="Good")
plt.bar(x,avg,width=0.5,label="Average",bottom=good)
plt.bar(x,exc,width=0.5,label="Excellent",bottom=avg+good)
plt.xticks(x,years,rotation=60)
plt.ylabel("Count of score category")
plt.xlabel("Release Year")
plt.title("Stacked Bar Chart")
plt.legend()
plt.tight_layout()
plt.savefig("score_category_stacked.png")
plt.show()

plt.hist(df["score"], bins=10, edgecolor="black")
plt.ylabel("Frequency")
plt.xlabel("score")
plt.title("Score Distribution")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.show()

# �� Part 5: Insights
# Identify:
# ● Which years had highest scores
#Around 2007–2011 had the highest number of high-rated games
# ● Whether high scores increased over time
#Excellent scores remain relatively rare compared to "Good"
# ● If editors_choice correlates with high scores
#"Excellent" has the highest probability of being editor’s choice
print(df.groupby("score_category")["editors_choice"].mean())