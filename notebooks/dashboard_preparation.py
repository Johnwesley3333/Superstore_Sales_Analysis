import pandas as pd
df = pd.read_csv("data/processed_sales_data.csv")
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
sales_by_category.to_csv('data/sales_by_category.csv', index=False)
profit_by_category.to_csv('data/profit_by_category.csv', index=False)
monthly_sales.to_csv('data/monthly_sales.csv', index=False)
