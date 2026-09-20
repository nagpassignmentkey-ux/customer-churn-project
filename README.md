# Telco Customer Churn Prediction Project

This is a Machine Learning solution designed to help a telecommunications company proactively identify customers who are likely to churn. 

---

## Project Structure

```text
customer_churn_project/
│
├── data/
│   └── TelcoCustomerChurn.csv
├── notebook/
│   └── churn_analysis.ipynb
├── model/
│   └── churn_model.pkl
├── app.py
├── requirements.txt
├── README.md
└── sample_request.json

## Steps to test

 1. Start the server using the "python app.py"
 2. This starts the server - listening on port 5000
 3. Try with samples request to get the needed predicition
 
 ```
 curl --location 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data '{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 1,
    "PhoneService": "Yes",
    "MultipleLines": "Yes",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "No",
    "Contract": "Two-Year",
    "PaperlessBilling": "No",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 100.35,
    "TotalCharges": 100.35
}'
 ``` 
