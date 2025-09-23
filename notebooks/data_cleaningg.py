import pandas as pd
df = pd.read_csv("data/raw_sales_data.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
df.to_csv("data/processed_sales_data.csv", index=False)
