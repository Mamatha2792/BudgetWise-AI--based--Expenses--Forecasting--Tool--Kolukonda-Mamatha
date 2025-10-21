# 💰 BudgetWise – AI-Based Expense Forecasting Tool

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.26-orange)
![License](https://img.shields.io/badge/License-MIT-green)

### 📊 Predict, Analyze & Plan Your Expenses Smarter!

**Developer:** Kolukonda Mamatha  
**College:** Sri Venkateswara College of Engineering, Tirupati  
## 🧠 Project Overview

An **AI-powered personal expense forecasting system** that predicts future spending patterns using machine learning. Features an interactive **Streamlit dashboard**, visualizations, and AI-driven insights for smarter financial planning.

---
## 🌟 Key Highlights  

- 🏆  **Champion Model (ARIMA):** Selected as the most accurate model for predicting daily spending with the lowest Mean Absolute Error (MAE).  
- 🤖 **Automated ML Pipeline:** End-to-end automation from data cleaning to model training and evaluation.  
- 🧠 **Multi-Model Benchmarking:** Benchmarks 4 different model families — Statistical, Random Forest, XGBoost, LightGBM — across 4 key metrics.  
- 📊 **Fully Interactive Dashboard:** Production-ready Streamlit app featuring KPIs, dynamic forecasting, budget optimization, and Plotly charts.  
- 💡**Data-Driven Insights:** Explore spending habits and visualize model performance transparently.  
- ⚙ **Professional & Modular Structure:** Clean project organization with dedicated folders for app, scripts, models, and utilities.  
-

## ⚡ Key Features

- **Accurate Forecasting:** Predicts 1-30 days of expenses  
- **Interactive Dashboard:** Production-ready Streamlit web app  
- **Data Insights:** Automated analysis of spending patterns  
- **Fast & Efficient:** Quick data processing and chart generation  
- **AI Recommendations:** Personalized suggestions based on spending  

---

## ✨ Core Features

| Feature | Description |
|---------|------------|
| Forecasting | Multi-model AI prediction (Linear Regression, ARIMA, LSTM) |
| Visualization | Interactive dashboards using Streamlit & Plotly |
| Data Upload | Upload and analyze expense CSV files |
| Download | Export prediction reports in CSV format |
| User-Friendly | Clean interface, responsive charts |

---

## 🧰 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly  
- **Model:** Linear Regression / ARIMA / LSTM  

---
## 📂 Project Structure  


personal_expense_forecasting/ <br>
├── 📂 app/ <br>
│   └── 📜 app.py <br>            
├── 📂 data/<br>
│   ├── 📂 raw/ <br>            
│   └── 📂 processed/ <br>      
├── 📂 models/<br>
│   └── 🏆 champion_model.pkl<br> 
├── 📂 notebooks/<br>
│   └── 🔬 ...               
├── 📂 scripts/<br>
│   ├── 📜 01_preprocess_data.py<br>  
│   ├── 📜 02_create_features.py<br>   
│   └── 📜 03_train_models.py<br>     
├── 📂 .streamlit/<br>
│   └── 📜 config.toml<br>         
├── 📜 .gitignore<br>
├── 📜 README.md<br>
└── 📜 requirements.txt<br>        

---
## 🚀 How to Run the Project

1. Clone the repository:
   
   git clone https://github.com/YourGitHubUsername/BudgetWise-AI-based-Expense-Forecasting-Tool.git
   cd BudgetWise-AI-based-Expense-Forecasting-Tool
   
2. Install required libraries:

   pip install -r requirements.txt

3. Run the Streamlit app:
   
   streamlit run app.py
   
4. Open your browser:

    http://localhost:8501
---

---

## 📸 Screenshots

   
| Dashboard View                                     | Forecast Result                                  |
| -------------------------------------------------- | ------------------------------------------------ |
| ![Dashboard Screenshot](screenshots/dashboard.png) | ![Forecast Screenshot](screenshots/forecast.png) |

---
## 🎯 Final Model Performance  

| Metric | *ARIMA* | Random Forest | XGBoost | LightGBM |
|:-------|:----------:|:--------------:|:--------:|:---------:|
| *MAE (₹)* | *34,008.95* | 40,765.15 | 220,219.29 | 7,281,243.57 |
| *RMSE (₹)* | *127,683.89* | 112,313.23 | 236,988.83 | 28,357,192.37 |
| *MAPE (%)* | *379.43* | 418.91 | 3,316.11 | 30,792.19 |
| *Directional Accuracy (%)* | 8.47 | *69.49* | 62.71 | 61.02 |

---
## 📈 Output Example

Input: User uploads past 6 months’ expense CSV file.
Output: Model predicts next 30 days’ expected spending and shows visual forecast charts.

## 🧑‍💻Skills Used

Data Preprocessing

Machine Learning

Data Visualization

Streamlit Web Development

 ## 🏁 Future Enhancements
Add income-expense ratio tracker

Enable real-time updates via APIs

Add login and user history tracking

