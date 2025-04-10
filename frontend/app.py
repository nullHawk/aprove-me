import streamlit as st
import requests

st.title("🏦 Loan Approval Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Marital Status", ["Unmarried", "Married"])
credit = st.selectbox("Credit History", ["Clear Debts", "Unclear Debts"])
income = st.number_input("Applicant Income", min_value=0)
loan_amt = st.number_input("Loan Amount", min_value=0)

if st.button("Predict"):
    payload = {
        "Gender": gender,
        "Married": married,
        "Credit_History": credit,
        "ApplicantIncome": income,
        "LoanAmount": loan_amt
    }
    try:
        response = requests.post("http://localhost:5000/prediction", json=payload)
        result = response.json()
        st.success(f"Loan Status: {result['loan_approval_status']}")
    except Exception as e:
        st.error(f"API Error: {e}")
