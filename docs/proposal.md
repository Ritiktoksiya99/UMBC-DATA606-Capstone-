# Diabetes Risk Prediction and Analysis Using Clinical and Lifestyle Factors

**Author:** Ritik Sunil Toksiya  
**Course:** UMBC DATA 606 – Capstone  
**Instructor:** Dr. Chaojie (Jay) Wang  

**GitHub Repository:** https://github.com/Ritiktoksiya99/UMBC-DATA606-Capstone-  
**LinkedIn Profile:** https://www.linkedin.com/in/ritik-toksiya/  
**PowerPoint Presentation:** To be added after presentation is created  
**YouTube Video:** To be added after project demo video is recorded  

---

## 1. Background

### What is this project about?

This project focuses on building a machine learning model to predict diabetes risk using clinical, demographic, and lifestyle factors collected from a large public health survey. The goal is to use structured survey data to classify individuals into diabetes risk categories based on their health indicators and behaviors.

The project is designed as a focused data science study that demonstrates data preprocessing, exploratory data analysis (EDA), model development, evaluation, and interpretation using a real-world healthcare dataset.

### Why does it matter?

Diabetes is among the most prevalent chronic diseases in the United States, affecting millions of people each year and placing a significant burden on the healthcare system and the economy. According to the Centers for Disease Control and Prevention (CDC), approximately 34.2 million Americans have diabetes and 88 million have prediabetes, with many individuals unaware of their condition or risk.

Early identification of high-risk individuals can:
- Encourage lifestyle changes such as improved diet and increased physical activity  
- Support early medical consultation and monitoring  
- Help public health officials target prevention efforts more effectively  

By leveraging a large public health dataset, this project demonstrates how machine learning can support preventive healthcare and population-level risk assessment.

---

## 2. Research Questions

- Can clinical, lifestyle, and demographic survey indicators be used to accurately predict diabetes risk?  
- Which factors (e.g., BMI, blood pressure, physical activity, smoking, age) are most predictive of diabetes?  
- How do different machine learning models (e.g., Logistic Regression, Random Forest, XGBoost) compare in performance for this task?  
- Can model interpretation techniques help explain the predictions in a meaningful way?  

---

## 3. Data

### Dataset Description

**Data Source:**  
The Diabetes Health Indicators Dataset derived from the Centers for Disease Control and Prevention (CDC) Behavioral Risk Factor Surveillance System (BRFSS) 2015, obtained from Kaggle.

The Behavioral Risk Factor Surveillance System (BRFSS) is a large-scale, nationwide health-related telephone survey conducted annually by the CDC in the United States. It collects responses from hundreds of thousands of adults on health-related risk behaviors, chronic health conditions, access to healthcare, and preventive health practices.

For this project, a cleaned and consolidated version of the BRFSS 2015 dataset is used, focusing on key clinical, lifestyle, and demographic indicators that are relevant to diabetes risk prediction in a **binary classification setting** (no diabetes vs. prediabetes/diabetes).

**Data Size:**  
Approximately 22.7 MB (CSV format)

**Data Shape:**  
The dataset contains **253,680 records** and **22 columns**, including one target variable and 21 predictor variables.

**Row Representation:**  
Each row represents an individual survey respondent’s health profile, including clinical indicators, lifestyle behaviors, and demographic attributes.

---

## Data Dictionary

| Column Name          | Data Type            | Definition                                                                 |
|----------------------|----------------------|-----------------------------------------------------------------------------|
| Diabetes_012         | Categorical (Target) | Diabetes status of the respondent                                           |
| HighBP               | Binary               | Indicates whether the respondent has high blood pressure                    |
| HighChol             | Binary               | Indicates whether the respondent has high cholesterol                       |
| CholCheck            | Binary               | Whether the respondent had a cholesterol check within the past 5 years      |
| BMI                  | Numeric              | Body Mass Index                                                             |
| Smoker               | Binary               | Indicates whether the respondent has smoked at least 100 cigarettes in life |
| Stroke               | Binary               | Indicates whether the respondent has ever been told they had a stroke       |
| HeartDiseaseorAttack | Binary               | History of coronary heart disease or myocardial infarction                  |
| PhysActivity         | Binary               | Indicates physical activity in the past 30 days (excluding work)            |
| Fruits               | Binary               | Indicates daily fruit consumption                                           |
| Veggies              | Binary               | Indicates daily vegetable consumption                                      |
| HvyAlcoholConsump    | Binary               | Indicates heavy alcohol consumption                                        |
| AnyHealthcare        | Binary               | Indicates whether the respondent has any form of healthcare coverage        |
| NoDocbcCost          | Binary               | Indicates inability to see a doctor due to cost in the past 12 months       |
| GenHlth              | Ordinal              | Self-reported general health status                                         |
| MentHlth             | Numeric              | Number of days mental health was not good in the past 30 days               |
| PhysHlth             | Numeric              | Number of days physical health was not good in the past 30 days             |
| DiffWalk             | Binary               | Indicates serious difficulty walking or climbing stairs                     |
| Sex                  | Binary               | Biological sex of the respondent                                            |
| Age                  | Ordinal              | Age group category of the respondent                                        |
| Education            | Ordinal              | Highest level of education completed                                        |
| Income               | Ordinal              | Annual household income category                                            |

---

## 4. Target and Predictors

**Target Variable:**  
- *Diabetes_binary*  
  - 0 = No diabetes  
  - 1 = Prediabetes or diabetes  

**Predictor Variables:**  
- Clinical indicators (e.g., BMI, HighBP, HighChol)  
- Lifestyle factors (e.g., Smoker, PhysActivity, diet, alcohol consumption)  
- Demographic factors (e.g., Age, Sex, Education, Income)  

---

## 5. Methodology (Proposed)

### Data Preprocessing
- Handle class imbalance  
- Encode categorical and ordinal variables  
- Scale numerical features if required  
- Split data into training and test sets  

### Exploratory Data Analysis (EDA)
- Study distributions of key variables  
- Analyze correlations  
- Compare feature distributions across diabetes classes  

### Modeling
- Baseline model: Logistic Regression  
- Tree-based models: Random Forest, XGBoost  
- Evaluation metrics: Accuracy, Precision, Recall, F1-score, ROC-AUC  

### Model Interpretation
- Feature importance analysis  
- Use of explainability methods (e.g., SHAP) to identify key risk factors  

### Deployment
- Build a simple web application using Streamlit  
- Integrate the trained machine learning model into the app  
- Allow users to input health indicators through a user-friendly interface  
- Display predicted diabetes risk along with basic explanatory insights  
- Use the deployment to demonstrate how the model can be used in a real-world, interactive setting  

---

## 6. Expected Outcomes

- A trained machine learning model that predicts diabetes risk from survey data  
- Identification of the most important clinical and lifestyle risk factors  
- A comparison of multiple machine learning models for this task  
- A deployed Streamlit web application demonstrating real-time diabetes risk prediction  
- Insights into how public health data can be used for population-level risk prediction  

---

## 7. Summary

This project applies machine learning techniques to a large public health dataset from the CDC’s BRFSS survey to predict diabetes risk using clinical, lifestyle, and demographic factors. The project emphasizes a focused and practical approach to data science, including preprocessing, modeling, evaluation, interpretation, and deployment, while addressing an important healthcare problem.
