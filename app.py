import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("credit_wise_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Credit Wise",
    page_icon="💳",
    layout="wide"
)

# Main heading
st.title("💳 Credit Wise")
st.subheader("Loan Approval Prediction System")

st.write(
    "Enter applicant details to predict loan approval."
)

st.divider()

# Applicant Information
st.header("Applicant Information")

col1, col2 = st.columns(2)

with col1:
    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0.0,
        value=10000.0
    )

    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0.0,
        value=2000.0
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    dependents = st.number_input(
        "Dependents",
        min_value=0,
        value=1
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=700
    )

    existing_loans = st.number_input(
        "Existing Loans",
        min_value=0,
        value=1
    )

with col2:
    dti_ratio = st.number_input(
        "DTI Ratio",
        min_value=0.0,
        value=0.30
    )

    savings = st.number_input(
        "Savings",
        min_value=0.0,
        value=10000.0
    )

    collateral_value = st.number_input(
        "Collateral Value",
        min_value=0.0,
        value=20000.0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        value=15000.0
    )

    loan_term = st.number_input(
        "Loan Term",
        min_value=1,
        value=60
    )

st.divider()

# Categorical Information
st.header("Additional Information")

col3, col4 = st.columns(2)

with col3:
    employment_status = st.selectbox(
        "Employment Status",
        ["Salaried", "Self-employed", "Contract", "Unemployed"]
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married"]
    )

    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Personal", "Car", "Business", "Home", "Education"]
    )

    property_area = st.selectbox(
        "Property Area",
        ["Urban", "Semiurban", "Rural"]
    )

with col4:
    education_level = st.selectbox(
        "Education Level",
        ["Graduate", "Not Graduate"]
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    employer_category = st.selectbox(
        "Employer Category",
        ["Private", "Government", "Unemployed", "MNC"]
    )

st.divider()

# Prediction Button
if st.button("Predict Loan Approval", type="primary"):

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "Applicant_Income": applicant_income,
        "Coapplicant_Income": coapplicant_income,
        "Age": age,
        "Dependents": dependents,
        "Credit_Score": credit_score,
        "Existing_Loans": existing_loans,
        "DTI_Ratio": dti_ratio,
        "Savings": savings,
        "Collateral_Value": collateral_value,
        "Loan_Amount": loan_amount,
        "Loan_Term": loan_term,
        "Employment_Status": employment_status,
        "Marital_Status": marital_status,
        "Loan_Purpose": loan_purpose,
        "Property_Area": property_area,
        "Education_Level": education_level,
        "Gender": gender,
        "Employer_Category": employer_category,
        "DTI_Ratio_sq": dti_ratio ** 2,
        "Credit_Score_sq": credit_score ** 2
    }])

    # Predict
    prediction = model.predict(input_data)

    # Display result
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("Loan Approved! 🎉")
    else:
        st.error("Loan Not Approved")

    # Prediction probability
    probabilities = model.predict_proba(input_data)[0]

    approval_probability = probabilities[
        list(model.classes_).index(1)
    ]

    st.metric(
        "Estimated Approval Probability",
        f"{approval_probability * 100:.2f}%"
    )

    st.caption(
        "This is an experimental ML prediction, "
        "not an actual bank lending decision."
    )
