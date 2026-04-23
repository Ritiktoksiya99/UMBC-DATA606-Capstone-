# Data

This folder contains the datasets used for the Diabetes Risk Prediction project.

## Dataset

### Diabetes Health Indicators Dataset

| Detail | Info |
|--------|------|
| File name | diabetes_health_indicators(1).csv |
| Source | CDC BRFSS 2015 via Kaggle |
| Download | https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset |
| Rows | 253,680 |
| Columns | 22 |

This dataset is derived from the CDC Behavioral Risk Factor Surveillance System (BRFSS) 2015 survey. It contains health indicators, lifestyle factors and demographic information collected from adults across the United States.

## Target Variable
- **0** = No Diabetes
- **1** = Prediabetes
- **2** = Diabetes

## Note
The original Kaggle dataset contains numeric values. For better readability during EDA, categorical labels were applied. The dataset was then re-encoded back to numeric values for model training.

## Setup Instructions
1. Download `diabetes_health_indicators(1).csv` from the Kaggle link above
2. Place the file in this `data/` folder
3. Run the notebook in the `notebooks/` folder
