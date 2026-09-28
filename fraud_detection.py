import streamlit as st
import pandas as pd
import joblib

#load in model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")

st.markdown("Please enter transaction details below to predict whether the transaction is fraudulent or not. Use the predict button to see the results.")

st.divider()

#Set inputs
transaction_type = st.selectbox("Transaction Type", ["DEBIT", "CASH_IN", "CASH_OUT", "PAYMENT", "TRANSFER"])
amount = st.number_input("Transaction Amount", min_value=0.0, value = 1000.0)

oldbalanceOrg = st.number_input("Old Balance of Origin Account (Sender)", min_value=0.0, value = 10000.0)
newbalanceOrig = st.number_input("New Balance of Origin Account (Sender)", min_value=0.0, value = 9000.0)

oldbalanceDest = st.number_input("Old Balance of Destination Account (Receiver)", min_value=0.0, value = 0.0)
newbalanceDest = st.number_input("New Balance of Destination Account (Receiver)", min_value=0.0, value = 0.0)

if st.button("Predict"):
    # Create a DataFrame with the input values
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction Result: {int(prediction)}")

    # Display result
    if prediction == 1:
        st.error("The transaction is predicted to be FRAUDULENT.")
    else:
        st.success("The transaction is predicted to be NOT FRAUDULENT.")