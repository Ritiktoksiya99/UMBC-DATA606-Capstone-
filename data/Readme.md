# Data

This folder contains the datasets used for the Diabetes Risk Prediction project.

## Datasets

### 1. Diabetes Health Indicators Dataset (Main Dataset)

| Detail | Info |
|--------|------|
| File name | diabetes_health_indicators(1).csv |
| Source | CDC BRFSS 2015 via Kaggle |
| Download | https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset |
| Rows | 253,680 |
| Columns | 22 |

Key columns: `Diabetes_012`, `HighBP`, `HighChol`, `BMI`, `Age`, `GenHlth`, `Income`

### 2. Diabetes Numeric Dataset (Encoded Version)

| Detail | Info |
|--------|------|
| File name | diabetes_numeric.csv |
| Source | Derived from diabetes_health_indicators(1).csv |
| Rows | 253,680 |
| Columns | 22 |

This file is the encoded version of the main dataset with all categorical variables converted to numeric values.

## Target Variable
- **0** = No Diabetes
- **1** = Prediabetes  
- **2** = Diabetes

## Setup Instructions
1. Download `diabetes_health_indicators(1).csv` from the Kaggle link above
2. Place the file in this `data/` folder
3. Run the notebook in the `notebooks/` folder
