# Data

This folder contains the datasets used for the Diabetes Risk Prediction project.

## Datasets

### 1. Diabetes Health Indicators Dataset (Categorical Version)

| Detail | Info |
|--------|------|
| File name | diabetes_health_indicators(1).csv |
| Source | CDC BRFSS 2015 via Kaggle |
| Download | https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset |
| Rows | 253,680 |
| Columns | 22 |

This is the human-readable version with categorical labels such as Yes/No, Male/Female, age groups and income brackets. Used for EDA and visualization.

### 2. Diabetes Numeric Dataset (Encoded Version)

| Detail | Info |
|--------|------|
| File name | diabetes_numeric.csv |
| Source | Derived from diabetes_health_indicators(1).csv |
| Rows | 253,680 |
| Columns | 22 |

This is the machine learning ready version with all categorical variables converted to numeric values using binary and ordinal encoding. Used for model training.

## Target Variable
- **0** = No Diabetes
- **1** = Prediabetes
- **2** = Diabetes

## Note
The original Kaggle dataset contains numeric values only. The categorical version was created by mapping numeric codes back to their descriptive labels for better readability during EDA.
