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

