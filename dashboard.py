import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

DB_URL = "sqlite:///retail_data.db"
engine = create_engine(DB_URL)

st.set_page_config(layout="wide")
st.title("Sales & Operations Dashboard")

monthly = pd.read_sql("SELECT * FROM monthly_sales ORDER BY order_month", engine)
region = pd.read_sql("SELECT * FROM region_sales", engine)
category = pd.read_sql("SELECT * FROM category_performance", engine)

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${monthly["total_sales"].sum():,.2f}")
col2.metric("Total Profit", f"${monthly["total_profit"].sum():,.2f}")

st.subheader("Monthly Sales Trend")
st.plotly_chart(px.line(monthly, x="order_month", y="total_sales", title="Monthly Sales Over Time"), use_container_width=True)

st.subheader("Regional Performance")
st.plotly_chart(px.bar(region, x="region", y="total_sales", color="region", title="Total Sales by Region"), use_container_width=True)

st.subheader("Category Profitability")
st.plotly_chart(px.scatter(category, x="total_sales", y="total_profit", size="avg_discount", color="category", title="Category Profitability"), use_container_width=True)

st.caption("Dataset: Gloabal Superstore (Kaggle)")
