import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

model = joblib.load(os.path.join(os.path.dirname(__file__), 'xgb_model.pkl'))
scaler = joblib.load(os.path.join(os.path.dirname(__file__), 'scaler.pkl'))

st.set_page_config(page_title='Diabetes Risk Predictor', page_icon='🩺', layout='wide')
st.title('🩺 Diabetes Risk Prediction App')
st.markdown('Enter your health indicators below to predict your diabetes risk.')

st.sidebar.header('Patient Information')
st.sidebar.subheader('BMI Calculator')
weight = st.sidebar.number_input('Weight (kg)', min_value=30.0, max_value=200.0, value=70.0)
height = st.sidebar.number_input('Height (cm)', min_value=100.0, max_value=250.0, value=170.0)
bmi = round(weight / ((height/100) ** 2), 1)
st.sidebar.metric('Your BMI', bmi)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Clinical Indicators')
    HighBP = st.selectbox('High Blood Pressure', ['No', 'Yes'])
    HighChol = st.selectbox('High Cholesterol', ['No', 'Yes'])
    CholCheck = st.selectbox('Cholesterol Check in last 5 years', ['No', 'Yes'])
    Stroke = st.selectbox('Ever had a Stroke', ['No', 'Yes'])
    HeartDiseaseorAttack = st.selectbox('Heart Disease or Attack', ['No', 'Yes'])
    DiffWalk = st.selectbox('Difficulty Walking', ['No', 'Yes'])

with col2:
    st.subheader('Lifestyle Factors')
    Smoker = st.selectbox('Smoker', ['No', 'Yes'])
    PhysActivity = st.selectbox('Physical Activity', ['No', 'Yes'])
    Fruits = st.selectbox('Daily Fruit Consumption', ['No', 'Yes'])
    Veggies = st.selectbox('Daily Vegetable Consumption', ['No', 'Yes'])
    HvyAlcoholConsump = st.selectbox('Heavy Alcohol Consumption', ['No', 'Yes'])
    AnyHealthcare = st.selectbox('Any Healthcare Coverage', ['No', 'Yes'])
    NoDocbcCost = st.selectbox('Could not see Doctor due to Cost', ['No', 'Yes'])

with col3:
    st.subheader('Demographics')
    GenHlth = st.selectbox('General Health', ['Excellent', 'Very good', 'Good', 'Fair', 'Poor'])
    MentHlth = st.slider('Bad Mental Health Days (last 30 days)', 0, 30, 0)
    PhysHlth = st.slider('Bad Physical Health Days (last 30 days)', 0, 30, 0)
    Sex = st.selectbox('Sex', ['Female', 'Male'])
    Age = st.selectbox('Age Group', ['18-24', '25-29', '30-34', '35-39', '40-44',
                                      '45-49', '50-54', '55-59', '60-64', '65-69',
                                      '70-74', '75-79', '80+'])
    Education = st.selectbox('Education Level', ['Never attended / Kindergarten',
                                                   'Grades 1-8', 'Grades 9-11',
                                                   'High school graduate / GED',
                                                   'Some college / Technical school',
                                                   'College graduate'])
    Income = st.selectbox('Income Level', ['< $10,000', '$10,000-$15,000',
                                            '$15,000-$20,000', '$20,000-$25,000',
                                            '$25,000-$35,000', '$35,000-$50,000',
                                            '$50,000-$75,000', '≥ $75,000'])

def encode_inputs():
    binary_map = {'Yes': 1, 'No': 0}
    genhlth_map = {'Excellent': 1, 'Very good': 2, 'Good': 3, 'Fair': 4, 'Poor': 5}
    age_map = {'18-24': 1, '25-29': 2, '30-34': 3, '35-39': 4, '40-44': 5,
               '45-49': 6, '50-54': 7, '55-59': 8, '60-64': 9, '65-69': 10,
               '70-74': 11, '75-79': 12, '80+': 13}
    education_map = {'Never attended / Kindergarten': 1, 'Grades 1-8': 2,
                     'Grades 9-11': 3, 'High school graduate / GED': 4,
                     'Some college / Technical school': 5, 'College graduate': 6}
    income_map = {'< $10,000': 1, '$10,000-$15,000': 2, '$15,000-$20,000': 3,
                  '$20,000-$25,000': 4, '$25,000-$35,000': 5, '$35,000-$50,000': 6,
                  '$50,000-$75,000': 7, '≥ $75,000': 8}

    if bmi < 18.5:
        bmi_category = 1
    elif bmi < 24.9:
        bmi_category = 2
    elif bmi < 29.9:
        bmi_category = 3
    else:
        bmi_category = 4

    health_score = MentHlth + PhysHlth
    lifestyle_risk = binary_map[Smoker] + binary_map[HvyAlcoholConsump] + (1 - binary_map[PhysActivity])

    data = {
        'HighBP': binary_map[HighBP],
        'HighChol': binary_map[HighChol],
        'CholCheck': binary_map[CholCheck],
        'BMI': bmi,
        'Smoker': binary_map[Smoker],
        'Stroke': binary_map[Stroke],
        'HeartDiseaseorAttack': binary_map[HeartDiseaseorAttack],
        'PhysActivity': binary_map[PhysActivity],
        'Fruits': binary_map[Fruits],
        'Veggies': binary_map[Veggies],
        'HvyAlcoholConsump': binary_map[HvyAlcoholConsump],
        'AnyHealthcare': binary_map[AnyHealthcare],
        'NoDocbcCost': binary_map[NoDocbcCost],
        'GenHlth': genhlth_map[GenHlth],
        'MentHlth': MentHlth,
        'PhysHlth': PhysHlth,
        'DiffWalk': binary_map[DiffWalk],
        'Sex': 1 if Sex == 'Male' else 0,
        'Age': age_map[Age],
        'Education': education_map[Education],
        'Income': income_map[Income],
        'BMI_Category': bmi_category,
        'Health_Score': health_score,
        'Lifestyle_Risk': lifestyle_risk
    }
    return pd.DataFrame([data])

if st.button('Predict Diabetes Risk', type='primary'):
    input_df = encode_inputs()
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]

    st.markdown('---')
    st.subheader('Prediction Result')

    if prediction == 0:
        st.success(f'✅ No Diabetes — Confidence: {probability[0]*100:.1f}%')
        st.markdown('**Recommendations:**')
        st.markdown('- Maintain your healthy lifestyle')
        st.markdown('- Continue regular physical activity')
        st.markdown('- Keep monitoring your BMI and blood pressure')

    elif prediction == 1:
        st.warning(f'⚠️ Prediabetes — Confidence: {probability[1]*100:.1f}%')
        st.markdown('**Recommendations:**')
        st.markdown('- Consult a doctor immediately')
        st.markdown('- Reduce sugar and carbohydrate intake')
        st.markdown('- Increase physical activity to at least 30 mins daily')
        st.markdown('- Monitor blood sugar levels regularly')

    else:
        st.error(f'🚨 Diabetes — Confidence: {probability[2]*100:.1f}%')
        st.markdown('**Recommendations:**')
        st.markdown('- Seek medical attention immediately')
        st.markdown('- Follow a strict diabetic diet')
        st.markdown('- Monitor blood sugar daily')
        st.markdown('- Take prescribed medications regularly')

    st.markdown('---')
    st.subheader('Your Risk Factor Summary')
    binary_map_local = {'Yes': 1, 'No': 0}
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('BMI', bmi)
    with col2:
        st.metric('Health Score', MentHlth + PhysHlth)
    with col3:
        st.metric('Lifestyle Risk Score',
                  binary_map_local[Smoker] + binary_map_local[HvyAlcoholConsump] + (1 - binary_map_local[PhysActivity]))
