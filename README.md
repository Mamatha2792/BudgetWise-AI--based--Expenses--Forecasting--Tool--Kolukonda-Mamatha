# 💰 BudgetWise – AI-Based Expense Forecasting Tool

> **"Predict tomorrow’s spending, plan today."**

BudgetWise is an intelligent web application that helps users **track, analyze, and forecast personal expenses** using **Machine Learning (ML) and AI** models.  
It transforms raw expense data into **smart insights, trends, and future predictions** through an interactive **Streamlit dashboard**.

---

## 🌟 Key Features

✅ **AI-Powered Predictions** – Uses ML models (XGBoost, Prophet, ARIMA, LSTM) to forecast daily/weekly/monthly expenses  
📊 **Interactive Dashboard** – Built with Streamlit for real-time visualization of spending patterns  
📈 **Smart Analytics** – Displays spending trends, category-wise summaries, and prediction accuracy  
📁 **Flexible Data Input** – Upload your own CSV files or use sample datasets  
🔒 **Secure & Local** – All data is processed locally; no external server or cloud storage required

---

## 🧠 Project Overview

| **Component**          | **Description**  |
|----------------|-----------------|
| **Frontend (UI)**       | Streamlit web dashboard |
| **Backend (ML Engine)** | Python (XGBoost, Prophet, ARIMA, LSTM) |
| **Dataset**             | CSV file with `date`, `amount`, `category` columns |
| **Output**              | Predicted expenses for upcoming days/weeks |
| **Evaluation Metrics**  | MAE, RMSE, MAPE, R², Directional Accuracy |

---

## 🏗️ Folder Structure

BudgetWise/
│
├── app/ # Streamlit dashboard files
│ └── budgetwise_app.py
│
├── models/ # Saved trained models (XGBoost, LSTM, etc.)
│
├── data/
│ ├── raw/ # Input expense data (CSV)
│ └── processed/ # Cleaned datasets
│
├── notebooks/ # Jupyter notebooks for training & experiments
│
├── scripts/ # Training or utility scripts
│
├── requirements.txt # Required Python libraries
└── launch_app.py # Script to run the Streamlit app


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YourUsername/BudgetWise-AI-based-Expense-Forecasting-Tool.git
cd BudgetWise-AI-based-Expense-Forecasting-Tool

2️⃣ Create and Activate Virtual Environment

Windows

python -m venv myvenv
.\myvenv\Scripts\Activate.ps1

Mac / Linux

python3 -m venv myvenv
source myvenv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the App

python launch_app.py
# or
streamlit run app/budgetwise_app.py --server.port 8502

Then open your browser → http://localhost:8502

📄 Example Input File

| date       | amount | category  | description       |
| ---------- | ------ | --------- | ----------------- |
| 2025-10-01 | 1200   | Groceries | Monthly groceries |
| 2025-10-03 | 250    | Transport | Cab + Bus fares   |
| 2025-10-05 | 800    | Utilities | Electricity bill  |


📊 Output Dashboard

✨ Forecast Graph – Shows next 7–30-day predictions
✨ Spending Trends – Compare current vs predicted
✨ Category Breakdown – Visual pie charts
✨ Model Comparison Table – MAE, RMSE, MAPE, R²

🧩 How It Works

  1. Data Upload – Import expense data (CSV)

  2. Data Preprocessing – Clean, remove nulls, convert dates

  3. Feature Engineering – Extract time-based features (day, month, rolling mean)

  4. Model Prediction – XGBoost (main), ARIMA/Prophet (baseline)

  5. Visualization – Streamlit dashboard renders analytics

  6. Recommendation Engine – Suggests saving insights & alerts

📈 Sample Results

| Model   | MAE  | RMSE | MAPE | R²    |
| ------- | ---- | ---- | ---- | ----- |
| XGBoost | 3.25 | 4.89 | 2.3% | 0.999 |
| LSTM    | 4.12 | 5.76 | 3.4% | 0.992 |
| Prophet | 5.10 | 6.23 | 4.1% | 0.985 |

(Values shown are sample results — actual accuracy depends on your data.)

🚀 Future Enhancements

🧠Planned Features (v2.0)
  📱 Mobile App: React Native mobile application
  🔌 API Integration: RESTful API for external system integration
  👥 Multi-user Support: Team collaboration and shared budgets
  📊 Advanced Analytics: More sophisticated financial insights
  🔄 Real-time Data: Live bank account integration
  🌐 Cloud Deployment: One-click cloud hosting options
🔬 Research & Development
  🧠 Advanced AI: Explore GPT-based financial advisors
  📈 Market Integration: Stock market and economic indicators
  🎯 Goal Tracking: Automated savings and budget goal monitoring
  🔍 Deeper Analytics: Merchant category analysis and recommendations

🧑‍💻 Tech Stack

Languages & Libraries:
Python, Streamlit, Pandas, NumPy, Matplotlib, XGBoost, Prophet, Scikit-learn

Tools:
Jupyter Notebook, VS Code, Git, Virtual Environment

❤️ Acknowledgements

We thank our mentors and open-source contributors for their support.
Inspired by the vision of empowering individuals with AI-driven financial awareness.


 🫧"Smart saving starts with smart forecasting — BudgetWise helps you stay ahead."
— Team BudgetWise🫧
