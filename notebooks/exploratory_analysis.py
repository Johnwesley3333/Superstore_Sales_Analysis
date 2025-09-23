import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("data/processed_sales_data.csv")
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='bar')
sns.scatterplot(x='Discount', y='Profit', data=df)
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar')
