# Diabetes Risk Prediction and Analysis Using Clinical and Lifestyle Factors

**Author:** Ritik Sunil Toksiya  
**Course:** UMBC DATA 606 – Capstone  
**Instructor:** Dr. Chaojie (Jay) Wang  

---

## 1. Background

### What is this project about?

This project focuses on building a machine learning model to predict diabetes risk using clinical, demographic, and lifestyle factors collected from a large public health survey. The goal is to use structured survey data to classify individuals into diabetes risk categories based on their health indicators and behaviors.

The project is designed as a focused data science study that demonstrates data preprocessing, exploratory analysis, model development, evaluation, and interpretation using a real-world healthcare dataset.

### Why does it matter?

Diabetes is among the most prevalent chronic diseases in the United States, affecting millions of people each year and placing a significant burden on the healthcare system and the economy. According to the Centers for Disease Control and Prevention (CDC), approximately 34.2 million Americans have diabetes and 88 million have prediabetes, with many individuals unaware of their condition or risk.

Early identification of high-risk individuals can:
- Encourage lifestyle changes such as improved diet and increased physical activity
- Support early medical consultation and monitoring
- Help public health officials target prevention efforts more effectively

By leveraging a large public health dataset, this project demonstrates how machine learning can support preventive healthcare and population-level risk assessment.

---

## 2. Research Questions

1. Can clinical and lifestyle survey indicators be used to accurately predict diabetes risk?
2. Which factors (e.g., BMI, blood pressure, physical activity, smoking, age) are most predictive of diabetes?
3. How do different machine learning models (e.g., Logistic Regression, Random Forest, XGBoost) compare in performance for this task?
4. Can model interpretation techniques help explain the predictions in a meaningful way?

---

## 3. Data

### Dataset Description

**Data Source:**  
Diabetes Health Indicators Dataset derived from the CDC’s Behavioral Risk Factor Surveillance System (BRFSS) 2015, available on Kaggle.

The Behavioral Risk Factor Surveillance System (BRFSS) is a health-related telephone survey conducted annually by the CDC. It collects responses from hundreds of thousands of Americans on health-related risk behaviors, chronic health conditions, and the use of preventive services.

For this project, a cleaned and consolidated version of the BRFSS 2015 dataset is used, which focuses on key indicators relevant to diabetes risk.

### Available Files

- `diabetes_012_health_indicators_BRFSS2015.csv`  
  - 253,680 records  
  - Target variable: `Diabetes_012` with three classes  
    - 0 = No diabetes (or only during pregnancy)  
    - 1 = Prediabetes  
    - 2 = Diabetes  
  - 21 feature variables  
  - Class imbalance is present  

- `diabetes_binary_5050split_health_indicators_BRFSS2015.csv`  
  - 70,692 records  
  - Balanced 50-50 split  
  - Target variable: `Diabetes_binary` (0 = No diabetes, 1 = Prediabetes or diabetes)  
  - 21 feature variables  

- `diabetes_binary_health_indicators_BRFSS2015.csv`  
  - 253,680 records  
  - Target variable: `Diabetes_binary` (not balanced)  
  - 21 feature variables  

For this project, the primary focus will be on the binary classification setting using the diabetes binary dataset.

---

### Features (Examples)

The dataset contains a mix of clinical, lifestyle, and demographic variables, including:

- BMI (Body Mass Index)
- HighBP (High blood pressure)
- HighChol (High cholesterol)
- Smoker
- PhysActivity (Physical activity)
- Fruits, Veggies (Diet indicators)
- HvyAlcoholConsump (Heavy alcohol consumption)
- GenHlth (General health, ordinal)
- MentHlth (Days of poor mental health)
- PhysHlth (Days of poor physical health)
- Age (Age group)
- Sex
- Education
- Income

---

## 4. Target and Predictors

**Target Variable:**  
- `Diabetes_binary`  
  - 0 = No diabetes  
  - 1 = Prediabetes or diabetes  

**Predictor Variables:**  
- Clinical indicators (e.g., BMI, HighBP, HighChol)
- Lifestyle factors (e.g., Smoker, PhysActivity, diet, alcohol consumption)
- Demographic factors (e.g., Age, Sex, Education, Income)

---

## 5. Methodology (Proposed)

1. Data preprocessing  
   - Handle class imbalance  
   - Encode categorical and ordinal variables  
   - Scale numerical features if required  
   - Split data into training and test sets  

2. Exploratory Data Analysis (EDA)  
   - Study distributions of key variables  
   - Analyze correlations  
   - Compare feature distributions across diabetes classes  

3. Modeling  
   - Baseline: Logistic Regression  
   - Tree-based models: Random Forest, XGBoost  
   - Evaluation metrics: Accuracy, Precision, Recall, F1-score, ROC-AUC  

4. Model Interpretation  
   - Feature importance analysis  
   - Use of explainability methods (e.g., SHAP) to identify key risk factors  

---

## 6. Expected Outcomes

- A trained machine learning model that predicts diabetes risk from survey data  
- Identification of the most important clinical and lifestyle risk factors  
- A comparison of multiple machine learning models for this task  
- Insights into how public health data can be used for population-level risk prediction  

---

## 7. Summary

This project applies machine learning techniques to a large public health dataset from the CDC’s BRFSS survey to predict diabetes risk using clinical, lifestyle, and demographic factors. The project emphasizes a focused and practical approach to data science, including preprocessing, modeling, evaluation, and interpretation, while addressing an important healthcare problem.

---

## 8. References

- Centers for Disease Control and Prevention (CDC), Behavioral Risk Factor Surveillance System (BRFSS)  
- Kaggle: Diabetes Health Indicators Dataset  
- Zidian Xie et al., *Building Risk Prediction Models for Type 2 Diabetes Using Machine Learning Techniques*
