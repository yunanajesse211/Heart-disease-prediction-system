import streamlit as st
import numpy as np
import pickle as pk
from PIL import Image

# Load the saved model
with open('model.pkl', 'rb') as f:
    lr = pk.load(f)

# Set up page navigation
menu = st.sidebar.selectbox("Navigation", ["Home", "Heart Disease Prediction"])

if menu == "Home":
    # Home page with app introduction and developer info
    st.title("Welcome to the Heart Disease Prediction System")
    
    st.write("""
    This app is designed to help predict the likelihood of heart disease based on patient data.
    The prediction is based on a **Neural Network machine learning model** trained on medical datasets.
    """)
    
    st.subheader("Developer")
    st.write("Developed by **ABAH JOHN**.")
    
    # Load and display the .ico image
    img = Image.open("heart.ico",)
    img = img.resize((700, 400))
    st.image(img, caption="Heart Disease Prediction", use_column_width=True)

elif menu == "Heart Disease Prediction":
    # Heart disease prediction page
    st.title("HEART DISEASE PREDICTION SYSTEM")

    # Form for user input
    with st.form("patient_form"):
        id_num = st.text_input("Enter Patient's ID")
        name = st.text_input("Enter Name")
        age = st.number_input("Enter Patient's Age", min_value=1, max_value=120, step=1)
        sex = st.selectbox("Select Gender", ('Male', 'Female'))
        chest_pain = st.selectbox("Feels severe chest pain", ('No', 'Yes', 'Yes not too severe', 'Very severe'))
        resting_bp = st.number_input("Enter Resting Blood Pressure level (mm Hg)", min_value=0, max_value=300, step=1)
        chol = st.number_input("Enter Cholestrol level (Mg/dl)", min_value=0, max_value=600, step=1)
        fast_bs = st.selectbox("Is sugar level greater than 120mg/dl?", ['Yes', 'No'])
        ecg = st.selectbox("Select ECG range", ['Normal[-0.5 to 0.4]', 'ST-T Abnormal[2.45 to 1.8]', 'Hypertrophy[1.4 to 2.8]'])
        heart_rate = st.number_input("Enter Max. heart rate", min_value=0, max_value=220, step=1)
        induced_cp = st.selectbox("Feeling severe chest pain after exercise", ['Yes', 'No'])
        peak = st.number_input("Depression Level after exercise relative to rest", min_value=0.0, max_value=100.0, step=0.1)
        slope = st.selectbox("Select slope shape", ['Up sloping', 'Flat', 'Down sloping'])
        ca = st.selectbox("Select Number of Major vessels", ['0', '1', '2', '3'])
        defect = st.selectbox("Select defect type", ['Normal', 'Fixed defect', 'Reversible defect'])

        # Submit button
        submitted = st.form_submit_button("View Result")

    # Processing the input data on form submission
    if submitted:
        # Convert the user input to numerical format for prediction
        sex_value = 1 if sex == 'Male' else 2
        chest_value = {'No': 0, 'Yes': 1, 'Yes not too severe': 2, 'Very severe': 3}[chest_pain]
        fast_bs_value = 1 if fast_bs == 'Yes' else 0
        ecg_value = {'Normal[-0.5 to 0.4]': 0, 'ST-T Abnormal[2.45 to 1.8]': 1, 'Hypertrophy[1.4 to 2.8]': 2}[ecg]
        induced_cp_value = 1 if induced_cp == 'Yes' else 0
        slope_value = {'Up sloping': 0, 'Flat': 1, 'Down sloping': 2}[slope]
        defect_value = {'Normal': 1, 'Fixed defect': 2, 'Reversible defect': 3}[defect]

        # Create a NumPy array with the inputs
        patient_details = np.array([[age, sex_value, chest_value, resting_bp, chol, fast_bs_value, ecg_value,
                                     heart_rate, induced_cp_value, peak, slope_value, int(ca), defect_value]])
        
        # Reshape and predict
        patient_details = patient_details.reshape(patient_details.shape[0], patient_details.shape[1], 1)
        
        # Make the prediction
        prediction = lr.predict(patient_details)

        # Display the result
        if prediction[0] == 1:
            st.success("Prediction: The patient is likely to have heart disease.")
        else:
            st.success("Prediction: The patient is unlikely to have heart disease.")
