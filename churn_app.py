
import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("churn_pipeline.pkl")

st.title("Customer Churn Prediction")

st.write("Enter customer details to predict churn risk")

# Numeric inputs
tenure = st.number_input("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# Categorical inputs 
gender = st.selectbox("Gender", ['Male','Female'])
partner = st.selectbox("Partner", ['Yes','No'])
dependents = st.selectbox("Dependents", ['Yes','No'])
phoneservice = st.selectbox("Phone Service", ['Yes','No'])
multiple = st.selectbox("Multiple Lines", ['Yes','No','No phone service'])

internet = st.selectbox("Internet Service", ['DSL','Fiber optic','No'])
online_sec = st.selectbox("Online Security", ['Yes','No','No internet service'])
online_backup = st.selectbox("Online Backup", ['Yes','No','No internet service'])
device = st.selectbox("Device Protection", ['Yes','No','No internet service'])
tech = st.selectbox("Tech Support", ['Yes','No','No internet service'])
stream_tv = st.selectbox("Streaming TV", ['Yes','No','No internet service'])
stream_movies = st.selectbox("Streaming Movies", ['Yes','No','No internet service'])

contract = st.selectbox("Contract", ['Month-to-month','One year','Two year'])
paperless = st.selectbox("Paperless Billing", ['Yes','No'])
payment = st.selectbox(
    "Payment Method",
    ['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)']
)

senior = st.selectbox("Senior Citizen", [0,1])

# Prediction 
if st.button("Predict Churn"):

    input_df = pd.DataFrame({
        'gender':[gender],
        'SeniorCitizen':[senior],
        'Partner':[partner],
        'Dependents':[dependents],
        'tenure':[tenure],
        'PhoneService':[phoneservice],
        'MultipleLines':[multiple],
        'InternetService':[internet],
        'OnlineSecurity':[online_sec],
        'OnlineBackup':[online_backup],
        'DeviceProtection':[device],
        'TechSupport':[tech],
        'StreamingTV':[stream_tv],
        'StreamingMovies':[stream_movies],
        'Contract':[contract],
        'PaperlessBilling':[paperless],
        'PaymentMethod':[payment],
        'MonthlyCharges':[monthly],
        'TotalCharges':[total]
    })

    proba = model.predict_proba(input_df)[0][1]

    # Threshold decision
    if proba > 0.35:
        st.error("High Risk of Churn")
    else:
        st.success("Low Risk")

    st.write(f"Churn Probability: {proba:.2f}")

   
    st.subheader("Suggestion")

    if proba > 0.35:
        st.write("Offer discounts, loyalty benefits, or proactive customer support to retain this customer.")
    else:
        st.write("Customer appears stable. Maintain engagement and service quality.")

