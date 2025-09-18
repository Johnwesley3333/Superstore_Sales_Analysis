import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("C:/Users/JOHN WESLEY/Downloads/archive (6)/Sample - Superstore.csv", encoding="latin-1")

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales & Revenue Dashboard")

# --- KPIs ---
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_order_value = df["Sales"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")

# --- Sidebar Filters ---
st.sidebar.header("Filters")
region = st.sidebar.multiselect("Select Region", df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Select Category", df["Category"].unique(), default=df["Category"].unique())

# Apply filters
filtered_df = df[(df["Region"].isin(region)) & (df["Category"].isin(category))]

# --- Monthly Sales Trend ---
monthly_sales = filtered_df.groupby(filtered_df["Order Date"].dt.to_period("M")).sum(numeric_only=True)["Sales"]
fig1 = px.line(x=monthly_sales.index.astype(str), y=monthly_sales.values,
               labels={"x": "Month", "y": "Sales"},
               title="Monthly Sales Trend")
st.plotly_chart(fig1, use_container_width=True)

# --- Sales by Region ---
fig2 = px.bar(filtered_df.groupby("Region")["Sales"].sum().reset_index(),
              x="Region", y="Sales", title="Sales by Region")
st.plotly_chart(fig2, use_container_width=True)

# --- Top 10 Products ---
top_products = filtered_df.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()
fig3 = px.bar(top_products, x="Sales", y="Product Name", orientation="h", title="Top 10 Products by Sales")
st.plotly_chart(fig3, use_container_width=True)
