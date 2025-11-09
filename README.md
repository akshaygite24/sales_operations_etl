# Sales and Operations ETL Pipeline

### End-to-End Data Engineering Project (Python • Pandas • SQLAlchemy • Streamlit • Airflow)

## Overview
This project simulates a real-world data engineering workflow for a retail company.
It automates the ETL (Extract, Transform, Load) process for the Global Superstore dataset
transforming raw sales data into insightful business metrics and visualizing them through an interactive dashboard.

## Tech Stack

| Layer              | Tool / Library                 | Purpose                         |
| ------------------ | ------------------------------ | ------------------------------- |
| Language        | **Python**                     | Core ETL logic                  |
| Data Processing | **Pandas, NumPy**              | Cleaning & transformation       |
| atabase       | **SQLite (SQLAlchemy)**        | Data storage & schema creation  |
| Orchestration   | **Apache Airflow**             | Daily ETL scheduling            |
| Visualization   | **Streamlit + Plotly**         | Interactive analytics dashboard |
| Dataset         | **Global Superstore (Kaggle)** | Real retail dataset             |


## Project Architecture

```
Global Superstore Dataset (CSV)
        │
        ▼
ETL Pipeline (Python, Pandas)
        │
        ▼
SQLite Database (retail_data.db)
        │
        ├── sales_raw
        ├── monthly_sales
        ├── region_sales
        └── category_performance
        ▼
Streamlit Dashboard (Sales & Operations KPIs)
        ▼
Apache Airflow DAG (Daily Automation)
```


## Folder Structure

```
sales_operations_etl/
├── data/
│   └── Superstore.csv
├── dags/
│   └── sales_ops_dag.py
├── etl_pipeline.py
├── dashboard.py
├── requirements.txt
├── .gitignore
├── retail_data.db
└── README.md

```

## ETL Pipeline
This script performs the complete ETL process:

1. Extract: Reads Superstore.csv (real dataset from Kaggle).

2. Transform:

    - Cleans and normalizes column names.

    - Calculates profit_margin, delivery_days, and order_month.

    - Aggregates data into monthly, regional, and category-level tables.

3. Load: Stores all tables in a local SQLite database (retail_data.db).

## Dashboard
`` File: dashboard.py ``

Run the dashboard:
```
streamlit run dashboard.py
```

## Features:

- Total Sales & Total Profit KPIs
- Monthly Sales Trend (Line Chart)
- Regional Sales Performance (Bar Chart)
- Category Profitability (Scatter Plot)

## Airflow Orchestration

File: `` dags/sales_ops_dag.py ``

DAG in this project automates the ETL workflow using Apache Airflow.
It runs daily (@daily) and uses a PythonOperator to execute the run_pipeline() function from your ETL script.

## How to Run the Project
### Setup Environment
```
python -m venv venv
venv\Scripts\activate        
pip install -r requirements.txt
```

### Run ETL
```
python etl_pipeline.py
```

### Launch Dashboard
```
streamlit run dashboard.py
```

### Deploy DAG in Airflow
```
# Place the DAG file into your Airflow dags directory
~/airflow/dags/sales_ops_dag.py
# Then start Airflow
airflow db migrate
airflow scheduler &
airflow webserver -p 8080
```

## Key Business KPIs
| Metric                           | Description                            |
| -------------------------------- | -------------------------------------- |
| **Total Sales**                  | Sum of all revenue by order            |
| **Total Profit**                 | Sum of profit across all sales         |
| **Profit Margin (%)**            | Profit/Sales × 100                     |
| **Average Delivery Days**        | Ship date − Order date                 |
| **Regional & Category Analysis** | Breakdown by location and product line |


## Author
### Akshay Gite
akshaygite2004@gmail.com
