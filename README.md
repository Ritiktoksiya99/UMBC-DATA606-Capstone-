# UMBC-DATA606-Capstone-
# Diabetes Risk Prediction and Analysis Using Clinical and Lifestyle Factors

**Author:** Ritik Sunil Toksiya  
**Program:** UMBC Data Science Master Degree Capstone — DATA606  
**Advisor:** Dr. Chaojie (Jay) Wang  
**Semester:** Spring 2026  

---

## Links
- [GitHub Repository](https://github.com/Ritiktoksiya99/UMBC-DATA606-Capstone-)
- [LinkedIn Profile](https://www.linkedin.com/in/ritik-toksiya/)
- [Live Streamlit App](https://5nrf2swp2buptpmwwiklxg.streamlit.app)
- [Project Proposal](docs/proposal.md)
- [Full Report](docs/report.md)
- [PowerPoint Presentation](https://docs.google.com/presentation/d/1k20b5UBP4FAW23bhAScNXH4WFKzHuA_C/edit?usp=sharing&ouid=118054097307591414694&rtpof=true&sd=true)
- YouTube Video: Coming soon

---

## Project Overview

Diabetes is one of the most prevalent chronic diseases in the United States, affecting approximately 34.2 million Americans with millions more unaware of their condition or risk. This project builds a machine learning model to predict diabetes risk using clinical, demographic and lifestyle factors collected from the CDC Behavioral Risk Factor Surveillance System (BRFSS) 2015 survey.

---

## Research Questions
1. Can clinical, lifestyle and demographic survey indicators accurately predict diabetes risk?
2. Which factors such as BMI, blood pressure, physical activity and age are most predictive of diabetes?
3. How do different machine learning models compare in performance for this task?
4. Can model interpretation techniques explain predictions in a meaningful way?

---

## Dataset
- **Source:** CDC BRFSS 2015 via Kaggle
- **Size:** 253,680 records, 22 features
- **Target Variable:** Diabetes_012 (0 = No Diabetes, 1 = Prediabetes, 2 = Diabetes)
- **Download:** https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

---

## Repository Structure
```
UMBC-DATA606-Capstone-/
├── app/                          # Streamlit web application
│   ├── app.py                    # Main Streamlit app script
│   ├── xgb_model.pkl             # Trained XGBoost model
│   ├── scaler.pkl                # Fitted StandardScaler
│   └── requirements.txt          # Required Python packages
├── data/                         # Dataset files
│   └── diabetes_health_indicators(1).csv
├── docs/                         # Project documentation
│   ├── proposal.md               # Project proposal
│   ├── report.md                 # Full project report
│   └── Ritik_Resume_Final.pdf    # Author resume
├── notebooks/                    # Jupyter notebooks
│   └── Capstone_Project_EDA_final.ipynb
└── README.md                     # This file
```
---

## Key Results

| Model | Testing Accuracy | CV Accuracy |
|-------|-----------------|-------------|
| Logistic Regression | 66.1% | 56.09% |
| Random Forest | 78.3% | 90.64% |
| **XGBoost** | **74.8%** | **72.11%** |

**Best Model: XGBoost** — most balanced performance with no overfitting

**Top Risk Factors (SHAP Analysis):** GenHlth, HighBP, Age, BMI, BMI_Category

---

## How to Run

### Jupyter Notebook
```bash
cd notebooks
jupyter notebook Capstone_Project_EDA_final.ipynb
```

### Streamlit App
```bash
cd app
pip install -r requirements.txt
streamlit run app.py
```

---

## Technologies Used
- **Languages:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, SHAP, Imbalanced-learn, Matplotlib, Seaborn, Streamlit, Joblib
- **Tools:** Jupyter Notebook, GitHub, Streamlit Cloud
