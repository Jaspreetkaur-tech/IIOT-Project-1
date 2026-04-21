# Customer Churn Prediction System - Project Overview

## Project Details
- **Environment**: Flask (Python)
- **Model**: XGBoost (model.pkl)
- **Frontend**: HTML5/CSS3 (Glassmorphism Design)

## Resolution Summary
1. **Directory Structure**: 
   - Moved template files into `templates/`
   - Moved styling files into `static/`
2. **Feature Alignment**: 
   - Expanded the prediction form to 19 features to match the model training.
   - Fixed the `ValueError: Feature shape mismatch` by ensuring strict ordering in `app.py`.
3. **UI Modernization**: 
   - Implemented a premium dark-mode design with responsive layout groups.

## How to Run
1. Ensure dependencies are installed: `pip install flask numpy xgboost`
2. Run the application: `python app.py`
3. Open in browser: `http://127.0.0.1:5000/`
