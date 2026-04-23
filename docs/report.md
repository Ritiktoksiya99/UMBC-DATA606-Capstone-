# Diabetes Risk Prediction and Analysis Using Clinical and Lifestyle Factors

**Author:** Ritik Sunil Toksiya  
**Program:** UMBC Data Science Master Degree Capstone — DATA606  
**Advisor:** Dr. Chaojie (Jay) Wang  
**Semester:** Spring 2026  

**Links:**
- [GitHub Repository](https://github.com/Ritiktoksiya99/UMBC-DATA606-Capstone-)
- [LinkedIn Profile](https://www.linkedin.com/in/ritik-toksiya/)
- [Streamlit App](https://5nrf2swp2buptpmwwiklxg.streamlit.app)
- PowerPoint Presentation: Coming soon
- YouTube Video: Coming soon

---

## 1. Background

### What is this project about?

This project focuses on building a machine learning model to predict diabetes risk using clinical, demographic, and lifestyle factors collected from a large public health survey. The goal is to use structured survey data to classify individuals into diabetes risk categories based on their health indicators and behaviors.

### Why does it matter?

Diabetes is among the most prevalent chronic diseases in the United States, affecting approximately 34.2 million Americans with millions more unaware of their condition or risk. Early identification of high-risk individuals can encourage lifestyle changes, support early medical consultation, and help public health officials target prevention efforts more effectively.

### Research Questions
1. Can clinical, lifestyle, and demographic survey indicators accurately predict diabetes risk?
2. Which factors such as BMI, blood pressure, physical activity and age are most predictive of diabetes?
3. How do different machine learning models compare in performance for this task?
4. Can model interpretation techniques explain predictions in a meaningful way?

---

## 2. Data

### Data Sources

**Diabetes Health Indicators Dataset**  
Source: CDC Behavioral Risk Factor Surveillance System (BRFSS) 2015 via Kaggle  
Download: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

### Dataset Overview

| Dataset | Rows | Columns | Source |
|---------|------|---------|--------|
| diabetes_health_indicators(1).csv | 253,680 | 22 | CDC BRFSS 2015 via Kaggle |

### Data Dictionary

| Column | Type | Description |
|--------|------|-------------|
| Diabetes_012 | Categorical | Target variable: 0=No Diabetes, 1=Prediabetes, 2=Diabetes |
| HighBP | Binary | High blood pressure indicator |
| HighChol | Binary | High cholesterol indicator |
| CholCheck | Binary | Cholesterol check in past 5 years |
| BMI | Numerical | Body Mass Index |
| Smoker | Binary | Smoked at least 100 cigarettes in lifetime |
| Stroke | Binary | Ever had a stroke |
| HeartDiseaseorAttack | Binary | History of heart disease or attack |
| PhysActivity | Binary | Physical activity in past 30 days |
| Fruits | Binary | Daily fruit consumption |
| Veggies | Binary | Daily vegetable consumption |
| HvyAlcoholConsump | Binary | Heavy alcohol consumption |
| AnyHealthcare | Binary | Has healthcare coverage |
| NoDocbcCost | Binary | Could not see doctor due to cost |
| GenHlth | Ordinal | Self-reported general health (1=Excellent to 5=Poor) |
| MentHlth | Numerical | Bad mental health days in past 30 days |
| PhysHlth | Numerical | Bad physical health days in past 30 days |
| DiffWalk | Binary | Difficulty walking or climbing stairs |
| Sex | Binary | Biological sex |
| Age | Ordinal | Age group category (1=18-24 to 13=80+) |
| Education | Ordinal | Highest education level (1-6) |
| Income | Ordinal | Annual household income category (1-8) |

### Target Variable
- **0** = No Diabetes — 213,703 samples (84.24%)
- **1** = Prediabetes — 4,631 samples (1.83%)
- **2** = Diabetes — 35,346 samples (13.93%)

### Data Quality Notes
The dataset contains no missing values across all 22 columns. The original Kaggle dataset contains numeric values. For better readability during EDA, categorical labels were applied. The dataset was then re-encoded back to numeric values using binary and ordinal encoding for model training.

---

## 3. Exploratory Data Analysis

All EDA was performed in Jupyter Notebook. The full notebook is available at: notebooks/Capstone_Project_EDA.ipynb

### Class Distribution
The target variable shows severe class imbalance — No Diabetes dominates at 84.24% while Prediabetes is severely underrepresented at only 1.83%. This imbalance required SMOTE oversampling before model training.

### Correlation Analysis
Pearson correlation analysis between all numeric features and the target variable revealed the following key findings:

- **GenHlth** has the strongest correlation with diabetes at r = 0.30
- **HighBP** correlates at r = 0.27
- **BMI** correlates at r = 0.22
- **DiffWalk** correlates at r = 0.22
- **HighChol** correlates at r = 0.21
- **Income** shows a negative correlation at r = -0.17 — higher income is associated with lower diabetes risk
- **PhysActivity** shows a negative correlation at r = -0.12 — physical activity is a protective factor

### Categorical Features Analysis
Respondents with High BP, High Cholesterol, Heart Disease and poor General Health show significantly higher diabetes rates. Age plays a major role with diabetes prevalence increasing steadily after age group 7 (50-54). Higher income and education levels are associated with lower diabetes rates.

### Numerical Features Analysis
BMI follows a right-skewed distribution with most respondents between 20-35. MentHlth and PhysHlth are heavily zero-inflated — most respondents report zero bad health days. Boxplot analysis shows diabetic respondents have a significantly higher median BMI (~31) compared to healthy respondents (~27).

### Key EDA Findings
- GenHlth, HighBP and BMI are the strongest clinical predictors of diabetes
- Age is a major demographic risk factor — diabetes risk increases steeply after 50
- Income and education show inverse relationships with diabetes risk
- Prediabetes class is severely underrepresented requiring special handling

---

## 4. Feature Engineering

The following features were engineered from the raw dataset:

| Feature | Formula | Purpose |
|---------|---------|---------|
| BMI_Category | pd.cut(BMI, bins=[0,18.5,24.9,29.9,100]) | Categorizes BMI into Underweight/Normal/Overweight/Obese |
| Health_Score | MentHlth + PhysHlth | Combined mental and physical health burden score |
| Lifestyle_Risk | Smoker + HvyAlcoholConsump + (1 - PhysActivity) | Combined unhealthy lifestyle indicator |

All three engineered features show positive correlation with the target variable — BMI_Category (0.21), Health_Score (0.16) and Lifestyle_Risk (0.10).

---

## 5. Model Training

### Data Preprocessing
- **Encoding:** Binary mapping (Yes=1, No=0) and ordinal encoding for GenHlth, Age, Education and Income
- **Train/test split:** 80/20 with stratification, random_state=42
- **SMOTE:** Applied on training data only to balance all three classes to 170,962 samples each
- **Feature Scaling:** StandardScaler applied to normalize all features to mean=0 and std=1

### Model Selection
Three classification models were evaluated:
- **Logistic Regression** — baseline linear model (max_iter=1000, class_weight='balanced')
- **Random Forest** — ensemble tree-based model (n_estimators=100, class_weight='balanced')
- **XGBoost** — gradient boosting model (n_estimators=100, eval_metric='mlogloss')

### Results

| Model | Training Accuracy | Testing Accuracy | CV Mean Accuracy |
|-------|------------------|-----------------|-----------------|
| Logistic Regression | 56.5% | 66.1% | 56.09% ± 0.30% |
| Random Forest | 99.2% | 78.3% | 90.64% ± 3.36% |
| XGBoost | 73.9% | 74.8% | 72.11% ± 3.59% |

**Best model: XGBoost with 74.8% testing accuracy**

### Classification Report

| Model | No Diabetes F1 | Prediabetes F1 | Diabetes F1 |
|-------|---------------|----------------|-------------|
| Logistic Regression | 0.78 | 0.04 | 0.43 |
| Random Forest | 0.78 | 0.04 | 0.44 |
| XGBoost | 0.85 | 0.03 | 0.42 |

### Feature Importance
SHAP analysis on the XGBoost model confirms that GenHlth, HighBP, Age and BMI are the most important features for diabetes prediction. Engineered features BMI_Category and Health_Score both appear in the top 10 confirming that feature engineering added value.

---

## 6. Streamlit Web Application

An interactive web application was built using Streamlit to make diabetes risk prediction accessible to anyone.

### Running the Application
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

### App Features
- **BMI Calculator** — Enter weight and height to auto-calculate BMI
- **Clinical Indicators** — Input High BP, High Cholesterol, Stroke history etc.
- **Lifestyle Factors** — Input smoking, physical activity, diet habits
- **Demographics** — Input age, sex, education and income
- **Prediction Result** — Shows No Diabetes, Prediabetes or Diabetes with confidence score
- **Recommendations** — Personalized health recommendations based on prediction
- **Risk Factor Summary** — Shows BMI, Health Score and Lifestyle Risk Score

### Live App
[https://5nrf2swp2buptpmwwiklxg.streamlit.app](https://5nrf2swp2buptpmwwiklxg.streamlit.app)

---

## 7. Conclusion

### Summary
This project demonstrates that diabetes risk can be predicted from CDC survey data using machine learning. An XGBoost model trained on 253,680 records achieves 74.8% testing accuracy with the most balanced performance across all three classes. SHAP analysis confirms that General Health status, High Blood Pressure, Age and BMI are the strongest predictors of diabetes risk.

The most significant challenge was the severe class imbalance — Prediabetes accounts for only 1.83% of the dataset. Despite applying SMOTE, all three models struggle to predict Prediabetes accurately (F1 scores below 0.05). This reflects a real-world challenge where prediabetes is often undiagnosed.

### Limitations
- **Class imbalance:** Prediabetes remains extremely difficult to predict due to severe underrepresentation
- **Temporal scope:** Dataset covers only 2015 — patterns may have changed
- **Binary features:** Many nuanced health factors are reduced to Yes/No

### Future Research Directions
- Explore LightGBM and CatBoost for potential improvement
- Apply cost-sensitive learning specifically for Prediabetes class
- Collect more recent CDC BRFSS data beyond 2015
- Add SHAP explanations directly into the Streamlit app
- Explore deep learning approaches for improved multiclass classification
- Investigate application barriers that may cause underdiagnosis of prediabetes

---

## 8. References

1. CDC BRFSS 2015 Dataset: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset
2. Centers for Disease Control and Prevention. National Diabetes Statistics Report. https://www.cdc.gov/diabetes/data
3. Pedregosa et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830.
4. Chen, T. and Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. KDD 2016.
5. Chawla, N.V. et al. (2002). SMOTE: Synthetic Minority Over-sampling Technique. Journal of Artificial Intelligence Research, 16, 321-357.
6. Lundberg, S.M. and Lee, S.I. (2017). A Unified Approach to Interpreting Model Predictions. NeurIPS 2017.
7. Streamlit Documentation: https://docs.streamlit.io/
8. pandas Documentation: https://pandas.pydata.org/docs/
9. Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5-32.
