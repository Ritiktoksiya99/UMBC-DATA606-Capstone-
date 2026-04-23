cat > /Users/ritiktoksiya/Downloads/Capstone_606/app/README.md << 'EOF'
# Diabetes Risk Prediction - Streamlit App

This folder contains the Streamlit web application for the Diabetes Risk Prediction project.

## Live App
[Click here to open the app](https://5nrf2swp2buptpmwwiklxg.streamlit.app)

## About the App
This app uses a trained XGBoost model to predict diabetes risk based on clinical, lifestyle and demographic indicators from the CDC BRFSS 2015 survey.

## Features
- **BMI Calculator** — Enter weight and height to auto-calculate BMI
- **Diabetes Risk Prediction** — Predicts No Diabetes, Prediabetes or Diabetes
- **Confidence Score** — Shows model confidence for the prediction
- **Recommendations** — Personalized health recommendations based on prediction
- **Risk Factor Summary** — Shows BMI, Health Score and Lifestyle Risk Score

## Files
| File | Description |
|------|-------------|
| app.py | Main Streamlit application script |
| xgb_model.pkl | Trained XGBoost model |
| scaler.pkl | Fitted StandardScaler for feature normalization |
| requirements.txt | Required Python packages |

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
The app will open at http://localhost:8501

## Dependencies
- streamlit
- pandas
- numpy==1.26.4
- scikit-learn
- xgboost
- joblib
EOF
