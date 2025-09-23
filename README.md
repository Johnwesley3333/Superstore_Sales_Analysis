# 🛒 Sales Analysis & Dashboard

*A comprehensive analysis and forecasting of retail sales data using Python.*

---

## 🌟 Overview
This project analyzes **retail sales data** to understand **sales trends, product performance, customer behavior, and profitability**. It also builds an **interactive dashboard** for real-time visualization and provides **forecasting insights** for future sales.  

**Key Objectives:**  
- Analyze sales performance over time.  
- Identify top-performing products, categories, and regions.  
- Examine the effect of discounts on profits.  
- Forecast future sales trends using time-series models.  
- Build an interactive **Streamlit dashboard** for decision-making.

---

## 📊 Dataset Overview
The dataset contains **order-level sales transactions** with attributes such as:  
- **Order ID** – Unique identifier for each order.  
- **Product Name** – Name of the sold product.  
- **Category & Sub-Category** – Product categories.  
- **Sales** – Revenue generated per transaction.  
- **Profit** – Profit earned per transaction.  
- **Discount** – Discount applied.  
- **Order Date** – Date of the order.  
- **Region / City** – Geographic location of the order.  

**Size:** Approximately X rows × Y columns (replace with actual numbers).

---

## 🎯 Project Workflow
✅ **Data Cleaning & Preprocessing** – Handle missing values, type conversions, duplicates, and feature creation.  
✅ **Feature Engineering** – Extract month, year, category-level summaries, and KPIs.  
✅ **Exploratory Data Analysis (EDA)** – Visualize sales trends across products, categories, and regions.  
✅ **Sales Forecasting** – Use **ARIMA / Prophet** models to predict future sales.  
✅ **Dashboard Creation** – Build an interactive **Streamlit dashboard** to explore KPIs, trends, and insights.

---

## 🛠️ Tech Stack
- **Programming Language:** Python 🐍  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly, Statsmodels, Prophet, Streamlit  
- **Tools:** Jupyter Notebook, Google Colab, GitHub  
- **Dashboarding:** Streamlit interactive dashboard  
- **Forecasting Models:** ARIMA / Prophet

---

## 📂 Project Structure
Superstore_Sales-Analysis/
├── Data
    ├── Raw
      ├── raw_sales_data.csv
    ├──cleaned
      ├── processed_sales_data.csv 
├── Notebooks
│   ├── data cleaning.ipynb
│   ├── expolratory_analysis.ipynb
│   ├── dashboard_preparation.ipynb
├──dashboards
     ├── sales_dashboard.py
├── Outputs/            # Sales insights and plots
│   ├── monthly sales Trend.png
│   ├── sales by city.png
│   ├── sales by region.png
│   ├── sales forecast top 10 products.png
├── requirements.txt           # Dependencies for the project
├── README.md                  # Project documentation
