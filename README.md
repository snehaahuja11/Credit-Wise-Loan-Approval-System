# Credit Wise: Loan Approval Prediction System

## Project Overview

Credit Wise is a Machine Learning-based Loan Approval Prediction System designed to predict whether a loan application is likely to be approved or rejected based on applicant financial and personal information.

The project explores different classification algorithms, compares their performance using evaluation metrics, and integrates the selected trained model into an interactive Streamlit web application.

## Key Features

- Loan approval prediction using Machine Learning.
- Exploratory Data Analysis (EDA) to understand applicant patterns.
- Data cleaning and missing value treatment.
- Categorical encoding and numerical feature scaling.
- Feature engineering to improve model representation.
- Comparison of multiple classification algorithms.
- Interactive Streamlit application for real-time predictions.
- Estimated loan approval probability.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Model Serialization | Joblib |
| Web Application | Streamlit |
| Development Environment | Jupyter Notebook, VS Code |

## Machine Learning Algorithms

The following classification algorithms were implemented and evaluated:

1. **Logistic Regression**
2. **K-Nearest Neighbors (KNN)**
3. **Gaussian Naive Bayes**

### Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

### Model Comparison

Based on the experimental results, the models achieved the following performance:

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Naive Bayes | 88.95% | 80.95% | 85.00% | 82.93% |
| Logistic Regression | 88.95% | 84.21% | 80.00% | 82.05% |
| KNN | 87.37% | 78.13% | 83.33% | 80.65% |

**Selected Model: Gaussian Naive Bayes**

Naive Bayes achieved the highest F1 Score among the three evaluated models.

## Project Structure

```text
Credit-Wise-Loan-Approval-System/
│
├── app.py
├── Project.ipynb
├── credit_wise_model.pkl
├── loan_approval_data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Streamlit Application

The project includes an interactive Streamlit interface where users can enter applicant information and receive:

- Loan approval prediction
- Estimated approval probability
- Prediction result displayed through an interactive interface

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/snehaahuja11/Credit-Wise-Loan-Approval-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Credit-Wise-Loan-Approval-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## Dataset

The project uses a loan approval dataset containing applicant-related information, including:

- Applicant Income
- Coapplicant Income
- Employment Status
- Age
- Marital Status
- Credit Score
- Existing Loans
- Debt-to-Income Ratio
- Savings
- Loan Amount
- Loan Term
- Loan Purpose
- Property Area
- Education Level
- Gender
- Employer Category

The target variable is `Loan_Approved`.

## Disclaimer

This project is developed for educational and machine learning experimentation purposes. Predictions are model-generated estimates and should not be considered actual financial advice or official bank lending decisions.



Machine Learning | Python | Data Science | Streamlit
