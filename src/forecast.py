# src/forecast.py
import numpy as np

def predict_future(model, df, periods=3):
    last = int(df['month_index'].max())
    future_idx = np.array([[i] for i in range(last+1, last+1+periods)])
    preds = model.predict(future_idx)
    # return list of floats
    return [float(round(x, 2)) for x in preds]

