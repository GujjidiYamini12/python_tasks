import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from scipy.stats import zscore
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("car_price_prediction.csv" , sep=",")
df.head()
df.info()
df.describe()


top_manufacturers = df['Manufacturer'].value_counts().nlargest(5).index

# Plot 1: Median Price per Manufacturer (Top 5)
plt.figure(figsize=(10, 6))
sns.barplot(x='Manufacturer', y='Price', data=df[df['Manufacturer'].isin(top_manufacturers)], estimator='median')
plt.title('Median Price per Manufacturer (Top 5)')
plt.xlabel('Manufacturer')
plt.ylabel('Median Price')
plt.show()

# Plot 3: Most Expensive Manufacturer (Top 5)
plt.figure(figsize=(8, 5))
sns.boxplot(x='Manufacturer', y='Price', data=df[df['Manufacturer'].isin(top_manufacturers)])
plt.title('Most Expensive Manufacturer (Top 5)')
plt.xlabel('Manufacturer')
plt.ylabel('Price')
plt.show()

# Plot 5: Manufacturer and Category (Top 5)
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Manufacturer', y='Price', hue='Category', data=df[df['Manufacturer'].isin(top_manufacturers)])
plt.title('Manufacturer and Category (Top 5)')
plt.xlabel('Manufacturer')
plt.ylabel('Price')
plt.legend(title='Category')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Color', data=df, order=df['Color'].value_counts().index, palette='viridis')
plt.title('Number of Cars per Color')
plt.xlabel('Color')
plt.ylabel('Number of Cars')
plt.show()

# Plot: Number of Cars per Fuel Type with Legend
plt.figure(figsize=(10, 6))
sns.countplot(x='Fuel type', data=df, order=df['Fuel type'].value_counts().index, palette='muted')
plt.title('Number of Cars per Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Cars')
plt.show()

# Plot: Number of Cars per Gear Box Type
plt.figure(figsize=(10, 6))
sns.countplot(x='Gear box type', data=df, order=df['Gear box type'].value_counts().index, palette='pastel')
plt.title('Number of Cars per Gear Box Type')
plt.xlabel('Gear Box Type')
plt.ylabel('Number of Cars')
plt.show()

# Plot 2: Number of Cars vs. Drive Wheels
plt.figure(figsize=(10, 6))
sns.countplot(x='Drive wheels', data=df, palette='viridis')
plt.title('Number of Cars vs. Drive Wheels')
plt.xlabel('Drive Wheels')
plt.ylabel('Number of Cars')
plt.show()


df.isnull().sum()


duplicates_id = df.duplicated(subset='ID', keep=False)
duplicated_rows = df[duplicates_id]
duplicated_rows_sorted = duplicated_rows.sort_values(by='ID')
duplicated_rows_sorted


df_no_duplicates_id = df.drop_duplicates(subset='ID')
df = df_no_duplicates_id
df


numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

Q1 = df[numerical_columns].quantile(0.25)
Q3 = df[numerical_columns].quantile(0.75)
IQR = Q3 - Q1

outliers = ((df[numerical_columns] < (Q1 - 1.5 * IQR)) | (df[numerical_columns] > (Q3 + 1.5 * IQR))).any(axis=1)
df = df[~outliers]
df



plt.figure(figsize=(16, 12))

plt.subplot(2, 2, 1)
sns.scatterplot(x='Prod. year', y='Price', data=df)
plt.title('Scatter Plot of Price vs. Prod. year')

plt.subplot(2, 2, 2)
sns.histplot(df['Price'], bins=30, kde=True)
plt.title('Histogram of Price')

df['Mileage'] = df['Mileage'].str.replace('km', '')

df['Mileage'] = df['Mileage'].astype(int)

df


def categorize_milage(milage):
    if milage < 100000:
        return 'Low'
    elif 100000 <= milage <= 300000:
        return 'Medium'
    else:
        return 'High'

df['Mileage_Category'] = df['Mileage'].apply(categorize_milage)


sns.countplot(x='Mileage_Category', data=df, palette='viridis')
plt.xlabel('Mileage Category')
plt.ylabel('Count')
plt.title('Distribution of Mileage Categories')
plt.show()

categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

ordinal_encoder = OrdinalEncoder()

encoded_data = ordinal_encoder.fit_transform(df[categorical_columns])

df[categorical_columns] = encoded_data.astype(int)

df.head()


all_columns = df.columns

num_cols = len(all_columns)
num_rows = (num_cols - 1) // 3 + 1  

fig, axes = plt.subplots(num_rows, 3, figsize=(20, 5 * num_rows))
fig.subplots_adjust(hspace=0.5)  

axes = axes.flatten()

for i, column in enumerate(all_columns):
    axes[i].hist(df[column], bins=25, edgecolor='black')
    axes[i].set_title(f'Histogram of {column}')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Frequency')

for i in range(num_cols, len(axes)):
    fig.delaxes(axes[i])

plt.show()


correlation_matrix = df.corr()
correlation_matrix

plt.figure(figsize=(20,20))
sns.heatmap(correlation_matrix, annot= True, linewidths= 0.5,cmap='hot')
plt.title('Correlation Heatmap')
plt.show()

price_correlations = correlation_matrix['Price'].drop('Price')
price_correlations_without_nan = price_correlations.dropna()
print("Correlations with Price (after dropping NaNs):")
print(price_correlations_without_nan)

X = df.drop('Price', axis=1)
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


models = [
    ('Random Forest', RandomForestRegressor()),
    ('Linear Regression', LinearRegression()),
    ('Gradient Boosting', GradientBoostingRegressor()),
    ('Ridge Regression', Ridge()),
    ('Lasso Regression', Lasso()),
    ('Decision Tree', DecisionTreeRegressor())
]

predictions = []

for model_name, model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    predictions.append((model_name, y_pred))
    

for model_name, y_pred in predictions:
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Model: {model_name}')
    print(f'Mean Squared Error: {mse:.2f}')
    print(f'R^2 Score: {r2:.2f}')
    print('--------------------------')



for model_name, y_pred in predictions:
    fig = plt.figure(figsize=(17, 10))
    plt.title(f"Prediction with {model_name}")
    plt.scatter(range(X_test.shape[0]), y_test, color='red', label='Real')
    plt.scatter(range(X_test.shape[0]), y_pred, marker='.', label='Predict')
    plt.legend(loc=2, prop={'size': 25})
    plt.show()



def show_predictions_for_all_models(X, Y, predictions):
  """Shows the predictions error for both the  algorithms and the actual value.

  Args:
    df: A Pandas DataFrame containing the actual values.
    predictions: A list of tuples containing the model name and predictions.

  Returns:
    A Pandas DataFrame containing the actual and predicted values errors for all the models.
  """

  df_actual_vs_predicted = pd.DataFrame()

  df_actual_vs_predicted['Actual'] = Y

  for model_name, y_pred in predictions:
    df_actual_vs_predicted[model_name] =  ((Y - y_pred).abs())

    
  df_actual_vs_predicted['Best Prediction Algorithm'] = df_actual_vs_predicted.drop('Actual', axis=1).idxmin(axis=1)

  # Get the numeric columns in the DataFrame
  numeric_columns =  df_actual_vs_predicted.select_dtypes(include='number').columns

  # Format the numeric columns as money
  for column in numeric_columns:
      df_actual_vs_predicted[column] =  df_actual_vs_predicted[column].apply(lambda x: f'${x:.2f}')

  return df_actual_vs_predicted


df_actual_vs_predicted = show_predictions_for_all_models(X_test, y_test, predictions)
df_actual_vs_predicted.head()


def calculate_best_prediction_counts_and_percentages(df):
  """Calculates the number of times each algorithm has the best prediction and the percentage of them.

  Args:
    df: A Pandas DataFrame containing the actual and predicted values for all the models.

  Returns:
    A Pandas DataFrame containing the number of times each algorithm has the best prediction and the percentage of them.
  """

  best_prediction_algorithm_column_name = df['Best Prediction Algorithm'].name

  best_prediction_counts = df[best_prediction_algorithm_column_name].value_counts()

  best_prediction_percentages = best_prediction_counts / len(df) * 100

  best_prediction_df = pd.DataFrame({'Best Prediction Algorithm': best_prediction_counts.index,
                                  'Count': best_prediction_counts.values,
                                  'Percentage': best_prediction_percentages.values})

  return best_prediction_df


best_prediction_df = calculate_best_prediction_counts_and_percentages(df_actual_vs_predicted)

best_prediction_df



best_prediction_algorithm_names = best_prediction_df['Best Prediction Algorithm'].tolist()

best_prediction_counts = best_prediction_df['Count'].tolist()

best_prediction_percentages = best_prediction_df['Percentage'].tolist()

plt.pie(best_prediction_counts, labels=best_prediction_algorithm_names, autopct='%1.1f%%')
plt.title('Pie Chart of Best Prediction Counts and Percentages')
plt.show()