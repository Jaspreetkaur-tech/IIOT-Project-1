from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # List of features in the exact order the model expects
    feature_names = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 
        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 
        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 
        'MonthlyCharges', 'TotalCharges'
    ]
    
    try:
        # Extract features from form data
        features = [float(request.form.get(name, 0)) for name in feature_names]
        final_features = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(final_features)
        
        if prediction[0] == 1:
            result = "Risk Level: High - Customer is likely to churn ❌"
        else:
            result = "Stability: High - Customer will likely stay ✅"
            
    except Exception as e:
        result = f"Error in prediction: {str(e)}"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)