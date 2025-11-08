import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DB_URL = "sqlite:///retail_data.db"
DATA_FILE = "data/Superstore.csv"

def extract():
    logging.info("Extracting dataset...")
    df = pd.read_csv(DATA_FILE)
    logging.info(f"Extracted {len(df)} rows.")
    return df

def transform(df):
    logging.info("Transforming data...")
    df.columns = df.columns.str.lower().str.replace(" ","_")
    df.dropna(subset=["order_date","sales","profit"], inplace=True)
    
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])
    df["profit_margin"] = np.where(df["sales"] != 0, (df["profit"] / df["sales"]) * 100, 0)
    df["delivery_days"] = (df["ship_date"] - df["order_date"]).dt.days
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

    monthly_sales = df.group("order_month").agg(
        total_sales = ("sales", "sum"),
        total_profit = ("profit", "sum")
        avg_margin = ("profit_margin", "mean")
        avg_delivery = ("delivery_days", "mean")
    ).reset_index()

    region_sales = df.groupby("region").agg(
        total_sales = ("sales", "sum"),
        total_profit = ("profit", "sum")
    ).reset_index()

    category_perf = df.groupby("category").agg(
        total_sales = ("sales", "sum"),
        total_profit = ("profit", "sum"),
        avg_discount = ("discount", "mean")
    ).reset_index()

    logging.info("Transformation complete.")
    return df, monthly_sales, region_sales, category_perf

def run_pipeline():
    df = extract()
    df_clean, monthly_sales, region_sales, category_perf =  transform(df)


if __name__ == "__main__":
    run_pipeline()