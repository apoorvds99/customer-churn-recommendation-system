# 📊 Customer Churn Recommendation System

An end-to-end Machine Learning project that predicts telecom customer churn and provides retention recommendations using a production-ready pipeline and an interactive Streamlit application.

---

## 🚀 Project Overview

Customer churn is a major business challenge for telecom companies.
This project builds a complete ML lifecycle solution that:

* analyzes churn patterns
* predicts churn probability
* applies business-driven decision thresholds
* provides actionable retention suggestions
* deploys predictions through an interactive Streamlit app

---

## 🎯 Key Highlights

* Exploratory Data Analysis and feature understanding
* Handling imbalanced data and evaluating multiple strategies
* Hyperparameter tuning and threshold optimization
* Production-ready preprocessing pipeline
* Probability-based churn decision system
* Interactive Streamlit deployment with recommendations

---

## 🧠 Model Approach

The final model uses:

* Logistic Regression with class imbalance handling
* Separate preprocessing for numeric and categorical features
* ColumnTransformer + Pipeline for reproducible transformations
* Probability threshold (0.35) optimized for churn recall

The threshold ensures high-risk customers are identified early for retention actions.

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Joblib

---
## 📂 Project Structure

```
customer-churn-recommendation-system/
│
├── Customer_Churn_Pred_Workflow.ipynb     # Research & experimentation notebook
├── Churn_pred_pipeline.ipynb              # Production pipeline training notebook
├── churn_app.py                               # Streamlit application
├── churn_pipeline.pkl                     # Saved trained pipeline model
├── Customer-Churn.csv                     # Dataset
├── requirements.txt                       # Project dependencies
└── README.md                              # Project documentation
```
---

## ▶️ Run the Streamlit App

Clone the repository:

```
git clone https://github.com/apoorvds99/customer-churn-recommendation-system.git
cd customer-churn-recommendation-system
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run churn_app.py
```

---

## 💡 Business Insight

The model identified strong retention indicators such as:

* long-term contracts
* higher tenure
* automatic payment methods
* multiple subscribed services

High churn signals include month-to-month contracts and electronic check payments.

---

## Author
Apoorv Singh
