import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = None

#1

try:
    file = input("Enter CSV file name: ")
    df = pd.read_csv(file)
    print("Dataset Loaded Successfully!")

    if df.isnull().values.any():
        print("Missing values found in the dataset.")
    else:
        print("No missing values found!")

except FileNotFoundError:
    print("File not found. Please check the file path!")
except Exception as e:
    print("Error loading data:", e)

#2

def calculate(df):
    if df is None:
        print("No file found!")
        return

    total = df['Total Sales'].sum()
    avg   = df['Total Sales'].mean()
    most_popular_product = df.loc[df['Total Sales'].idxmax(), 'Product']

    print("\nSales Metrics")
    print("Total sales:", total)
    print("Average sales:", avg)
    print("Most Popular Product:", most_popular_product)

calculate(df)

#3

growth = df['Growth Rate (%)'] = df['Total Sales'].pct_change() * 100

print(df)

sales_by_category = df.groupby('Category')['Total Sales'].sum()
print("\nTotal sales by Category:")
print(sales_by_category)

sales_by_date = df.groupby('Date')['Total Sales'].sum()
print("\nTotal sales by Date:")
print(sales_by_date)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,6))
sns.barplot(x=sales_by_category.index, y=sales_by_category.values, palette="viridis")
plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

plt.figure(figsize=(10,6))
sns.lineplot(x=sales_by_date.index, y=sales_by_date.values, marker="o")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(6,5))
corr = df[['Price','Quantity Sold']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation between Price and Quantity Sold")
plt.show()

