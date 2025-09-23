Sales-Analysis-Dashboard/
├── README.md
│
│   # 🛒 Sales Analysis & Dashboard
│
│   *A comprehensive analysis and forecasting of retail sales data using Python.*
│
│   ---
│
│   ## 🌟 Overview
│   This project analyzes retail sales data to understand sales trends, product performance, customer behavior, and profitability.
│   It also builds an interactive dashboard and provides forecasting insights for future sales.
│
│   ---
│
│   ## 📊 Dataset Overview
│   - Order ID – Unique identifier
│   - Product Name – Sold product
│   - Category & Sub-Category
│   - Sales – Revenue per transaction
│   - Profit – Profit per transaction
│   - Discount – Discount applied
│   - Order Date – Date of transaction
│   - Region / City – Geographic location
│
│   ---
│
│   ## 🎯 Project Workflow
│   1. Data Cleaning & Preprocessing
│   2. Feature Engineering
│   3. Exploratory Data Analysis (EDA)
│   4. Sales Forecasting (ARIMA / Prophet)
│   5. Dashboard Creation (Streamlit)
│
│   ---
│
│   ## 🛠️ Tech Stack
│   - Python
│   - Pandas, NumPy, Matplotlib, Seaborn, Plotly
│   - Statsmodels, Prophet, Streamlit
│
│   ---
│
│   ## 📂 Project Structure
│   ```
│   Sales-Analysis-Dashboard/
│   ├── data/
│   │   ├── raw_sales_data.csv
│   │   └── processed_sales_data.csv
│   ├── notebooks/
│   │   ├── 01_data_cleaning.ipynb
│   │   ├── 02_exploratory_analysis.ipynb
│   │   └── 03_dashboard_preparation.ipynb
│   ├── dashboards/
│   │   └── sales_dashboard.py
│   ├── outputs/
│   │   ├── plots/
│   │   └── reports/
│   ├── requirements.txt
│   └── README.md
│   ```
│
│   ---
│
│   ## 🚀 Installation & Setup
│   ```bash
│   git clone https://github.com/Johnwesley3333/Sales-Analysis-Dashboard.git
│   cd Sales-Analysis-Dashboard
│   pip install -r requirements.txt
│   streamlit run dashboards/sales_dashboard.py
│   ```
│
│   ---
│
│   ## 📈 Key Insights & Forecasting
│   - Monthly & yearly sales trends
│   - Top products, categories, regions
│   - Discount vs Profit analysis
│   - Forecast future sales with ARIMA / Prophet
│
│   ---
│
│   ## 📉 Conclusion
│   Provides a data-driven approach to understanding sales trends and predicting future performance.
│
│   ---
│
│   ## 🤝 Contributions
│   1. Fork the repository
│   2. Create a branch
│   3. Submit a Pull Request
│
│   ---
│
│   ## 📩 Connect
│   - GitHub: [Johnwesley3333](https://github.com/Johnwesley3333)
│   - Email: your-email@example.com
│
├── requirements.txt
│   pandas==2.1.1
│   numpy==1.26.2
│   matplotlib==3.8.0
│   seaborn==0.12.2
│   plotly==6.1.0
│   streamlit==1.28.0
│   scikit-learn==1.3.0
│   statsmodels==0.14.1
│   prophet==1.1.4
│   openpyxl==3.1.3
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   │   import pandas as pd
│   │   df = pd.read_csv("data/raw_sales_data.csv")
│   │   df['Order Date'] = pd.to_datetime(df['Order Date'])
│   │   df['Month'] = df['Order Date'].dt.month
│   │   df['Year'] = df['Order Date'].dt.year
│   │   df.to_csv("data/processed_sales_data.csv", index=False)
│   │
│   ├── 02_exploratory_analysis.ipynb
│   │   import pandas as pd
│   │   import matplotlib.pyplot as plt
│   │   import seaborn as sns
│   │   df = pd.read_csv("data/processed_sales_data.csv")
│   │   monthly_sales = df.groupby('Month')['Sales'].sum()
│   │   monthly_sales.plot(kind='bar')
│   │   sns.scatterplot(x='Discount', y='Profit', data=df)
│   │   top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
│   │   top_products.plot(kind='bar')
│   │
│   ├── 03_dashboard_preparation.ipynb
│       import pandas as pd
│       df = pd.read_csv("data/processed_sales_data.csv")
│       sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
│       profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()
│       monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
│       sales_by_category.to_csv('data/sales_by_category.csv', index=False)
│       profit_by_category.to_csv('data/profit_by_category.csv', index=False)
│       monthly_sales.to_csv('data/monthly_sales.csv', index=False)
│
├── dashboards/
│   └── sales_dashboard.py
│       import streamlit as st
│       import pandas as pd
│       import plotly.express as px
│       st.set_page_config(page_title="Sales Dashboard", layout="wide")
│       df = pd.read_csv("data/processed_sales_data.csv")
│       st.title("🛒 Superstore Sales Dashboard")
│       total_sales = df['Sales'].sum()
│       total_profit = df['Profit'].sum()
│       avg_discount = df['Discount'].mean()
│       st.metric("Total Sales", f"${total_sales:,.0f}")
│       st.metric("Total Profit", f"${total_profit:,.0f}")
│       st.metric("Average Discount", f"{avg_discount:.2%}")
│       sales_category = df.groupby('Category')['Sales'].sum().reset_index()
│       fig = px.bar(sales_category, x='Category', y='Sales', color='Category')
│       st.plotly_chart(fig, use_container_width=True)
│       monthly_sales = df.groupby(df['Order Date'].str[:7])['Sales'].sum().reset_index()
│       monthly_sales.columns = ['Month', 'Sales']
│       fig2 = px.line(monthly_sales, x='Month', y='Sales', markers=True)
│       st.plotly_chart(fig2, use_container_width=True)
│       fig3 = px.scatter(df, x='Discount', y='Profit', color='Category', hover_data=['Product Name'])
│       st.plotly_chart(fig3, use_container_width=True)
