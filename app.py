# app.py
from src.data_preprocessing import load_data
from src.model import train_simple_model
from src.forecast import predict_future
import matplotlib.pyplot as plt

def main():
    # Load data
    df = load_data("data/expenses.csv")
    
    # Train model
    model = train_simple_model(df)
    
    # Predict next 3 months
    future_months = 3
    preds = predict_future(model, df, periods=future_months)
    
    print("Next 3 predicted expenses:", preds)
    
    # Prepare data for plotting
    past_months = df['month'].tolist()
    past_expenses = df['expense'].tolist()
    
    # Future months labels (e.g., 2024-11, 2024-12, 2025-01)
    last_month_index = df['month_index'].max()
    last_month_str = df['month'].iloc[-1]
    year, month = map(int, last_month_str.split('-'))
    future_month_labels = []
    for i in range(future_months):
        month += 1
        if month > 12:
            month = 1
            year += 1
        future_month_labels.append(f"{year:04d}-{month:02d}")
    
    # Combine past + predicted
    all_months = past_months + future_month_labels
    all_expenses = past_expenses + preds
    
    # Plot
    plt.figure(figsize=(10,5))
    plt.plot(past_months, past_expenses, marker='o', label='Past Expenses')
    plt.plot(future_month_labels, preds, marker='x', linestyle='--', color='red', label='Predicted Expenses')
    plt.title("Monthly Expenses Forecast")
    plt.xlabel("Month")
    plt.ylabel("Expense")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
    # Wrapper function to predict expense
def predict_expense(income, savings, expenses):
    # Replace below with your actual model code from app.py
    # Example placeholder logic:
    result = income + savings - expenses
    return result

