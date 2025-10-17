# src/model.py
from sklearn.linear_model import LinearRegression
import numpy as np

def train_simple_model(df):
    # expects df with 'month_index' and 'expense'
    X = df[['month_index']].values
    y = df['expense'].values
    model = LinearRegression()
    model.fit(X, y)
    return model

