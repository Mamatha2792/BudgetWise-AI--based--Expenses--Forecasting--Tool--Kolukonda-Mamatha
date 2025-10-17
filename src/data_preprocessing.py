# src/data_preprocessing.py
import pandas as pd

def load_data(path="data/expenses.csv"):
    df = pd.read_csv(path)
    # ensure numeric month_index and expense
    df['month_index'] = df['month_index'].astype(int)
    df['expense'] = df['expense'].astype(float)
    return df

