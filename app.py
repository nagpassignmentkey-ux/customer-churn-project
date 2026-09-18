from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model pipeline
model = joblib.load('model/churn_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        # Convert JSON to DataFrame
        df_input = pd.DataFrame([data])
        
        # Apply identical feature engineering
        df_input['TotalCharges'] = pd.to_numeric(df_input['TotalCharges'], errors='coerce').fillna(0)
        df_input['AverageMonthlySpend'] = df_input['TotalCharges'] / (df_input['tenure'] + 1)
        
        service_cols = [
            'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 
            'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'
        ]
        df_input['TotalServicesCount'] = df_input[service_cols].apply(
            lambda col: col.isin(['Yes']).astype(int)
        ).sum(axis=1)
        
        # Predict
        prediction_encoded = model.predict(df_input)[0]
        prediction_label = 'Yes' if prediction_encoded == 1 else 'No'
        churn_proba = float(model.predict_proba(df_input)[0][1])
        
        return jsonify({
            "prediction": prediction_label,
            "churn_probability": round(churn_proba, 2)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
