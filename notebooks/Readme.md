# Notebooks

This folder contains the Jupyter notebooks for the Diabetes Risk Prediction capstone project.

## Files

| File | Description |
|------|-------------|
| Capstone_Project_EDA_final.ipynb | Main notebook covering full EDA, feature engineering, encoding, SMOTE, feature scaling, model training, evaluation, SHAP analysis and cross validation |

## Notebook Contents

1. **Project Overview** — Background, dataset description and research questions
2. **Exploratory Data Analysis** — Class distribution, categorical features, numerical features, boxplots
3. **Correlation Heatmap** — Feature correlations with target variable
4. **Feature Encoding** — Binary and ordinal encoding of all categorical variables
5. **Feature Engineering** — BMI_Category, Health_Score and Lifestyle_Risk
6. **Class Imbalance** — SMOTE oversampling to balance all three classes
7. **Feature Scaling** — StandardScaler normalization
8. **Model Training** — Logistic Regression, Random Forest and XGBoost
9. **Classification Report** — Precision, Recall and F1-Score for all models
10. **Confusion Matrix** — Prediction error visualization
11. **ROC Curve** — Multiclass ROC curve comparison
12. **Feature Importance** — Random Forest and XGBoost feature importance
13. **SHAP Analysis** — Model interpretability using SHAP values
14. **Cross Validation** — 5-fold cross validation for all models
15. **Conclusion** — Summary of findings and next steps

## How to Run

```bash
cd notebooks
jupyter notebook Capstone_Project_EDA_final.ipynb
```

Make sure the dataset `diabetes_health_indicators(1).csv` is placed in the `data/` folder before running.
