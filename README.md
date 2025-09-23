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
```
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
```

---

## 🚀 Installation & Setup
1️⃣ **Clone the repository**  
```bash
git clone https://github.com/Johnwesley3333/Superstore_Sales-Analysis-Dashboard.git
cd Sales-Analysis-Dashboard
```
2️⃣ Install dependencies
```
pip install -r requirements.txt
```
3️⃣ Run the Streamlit dashboard
```
streamlit run dashboards/sales_dashboard.py
```
4️⃣ Open your browser at http://localhost:8501 to explore the dashboard.
## 📈 **Key Insights & Forecasting**
### **Exploratory Data Analysis (EDA)**
- **Monthly Sales Trends** – Identifies peak sales periods.
- **Sales by City** – Highlights the most profitable locations.
- **Sales by Hour** – Finds optimal sales hours for targeted marketing.

### **Sales Forecasting Results (ARIMA Model)**
| Month        | Forecasted Sales ($) |
|-------------|--------------------|
| February 2020 | 2,908,670 |
| March 2020    | 336,821 |
| April 2020    | 2,617,652 |
| May 2020      | 594,909 |
| June 2020     | 2,388,767 |
| July 2020     | 797,894 |
| August 2020   | 2,208,752 |
| September 2020 | 957,540 |
| October 2020  | 2,067,170 |
| November 2020 | 1,083,101 |
| December 2020 | 1,955,817 |
| January 2021  | 1,181,854 |

## 📉 **Conclusion**
This project provides a **data-driven approach** to understanding sales trends and forecasting future performance. The **ARIMA model** effectively predicts sales, offering valuable insights for **business decision-making and strategy planning**.

## 🤝 **Contributions**
💡 Open to improvements! Feel free to:
1. Fork the repo  
2. Create a new branch (`feature-branch`)  
3. Make changes & submit a PR  



## 📩 **Connect with Me**
📧 **Email:** [johnwesleykolasanakoti@gmail.com](mailto:johnwesleykolasanakoti@gmail.com)  
🌐 **Portfolio:** [K-John Wesley Portfolio]()  
💼 **LinkedIn:** [K-John Wesley](www.linkedin.com/in/john-wesley-794125284)  
👨‍💻 **GitHub:** [K- John Wesley](https://github.com/Johnwesley3333)  

⭐ **If you find this project useful, drop a star!** 🚀
