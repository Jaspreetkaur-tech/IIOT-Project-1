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
    data = request.form.to_dict()

    features = [float(x) for x in data.values()]
    final = np.array(features).reshape(1, -1)

    prediction = model.predict(final)

    if prediction[0] == 1:
        result = "Customer is likely to churn ❌"
    else:
        result = "Customer will stay ✅"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)