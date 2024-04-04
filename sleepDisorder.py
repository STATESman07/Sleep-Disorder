import streamlit as st
import pickle as pk
import numpy as np
from PIL import Image

users_data = []

# setting size of images
########################################Sleep_Disorder Change Size ################################################
Sleep_Disorder = Image.open('SleepDisorder.png')
new_image = Sleep_Disorder.resize((650, 250))

#########################################           FIT         ###############################################
fit = Image.open("fit.jpg")
new_fit = fit.resize((700, 400))

#########################################           Sleep Apnea          ###############################################
Sleep_Apnea = Image.open("apena.jpg")
new_apenea = Sleep_Apnea.resize((700, 450))

#########################################           Insomania          ###############################################
insomnia = Image.open("insomnia.jpg")
new_insomnia = insomnia.resize((700, 450))

st.image(new_image)


#################################### Ecoding Occupation ######################################
def encode_occ(occ, occ_list):
    output = [0, 0, 0, 0, 0]
    if occ not in occ_list:
        return output
    else:
        index = occ_list.index(occ)
        output[index] = 1
        return output


############################################### Giving data to SESSON #######################################
def data_display(name, gender, age, Sleep_Duration, Sleep_Quality, PhysicalActivity,
                 stress, BMI, HeartRate, steps, pressureHigh, pressureLow, occupation):
    st.session_state.name = name
    st.session_state.age = age
    st.session_state.gender = gender
    st.session_state.occupation = occupation
    st.session_state.Sleep_Duration = Sleep_Duration
    st.session_state.Sleep_Quality = Sleep_Quality
    st.session_state.PhysicalActivity = PhysicalActivity
    st.session_state.stress = stress
    st.session_state.bmi = BMI
    st.session_state.heartRate = HeartRate
    st.session_state.steps = steps
    st.session_state.pressureH = pressureHigh
    st.session_state.pressureL = pressureLow


###############################################  Buttons SUBMIT AND BACk#############################################
def data_entry():
    st.session_state.users_data = users_data
    st.session_state.page = 'Prediction Page'


def back_page1():
    st.session_state.page = 'Input Page'


###################################getting input###############################################
def input_page():

    # Name
    st.header("Name")
    name = st.text_input("Enter your name:")

    # Gender
    st.header("Gender")
    gender = st.radio("Gender", ["Male", "Female"], horizontal=True)

    # Age
    st.header("Age")
    age = st.slider('Your Age', min_value=25, max_value=60, value=None)

    # Occupation
    st.header("Occupation")
    occupation = st.selectbox("What do you do?",
                              ["Software Engineer", "Doctor", "Nurse", "Lawyer", "Teacher", "Others"])

    # Sleep Duration
    st.header("Sleep Duration")
    Sleep_Duration = st.number_input("Sleep Duration:", min_value=4.0, max_value=10.0)

    # Sleep Quality
    st.header("Sleep Quality")
    Sleep_Quality = st.slider('Quality of sleep', min_value=2, max_value=10, value=5)

    # Physical Activity Level
    st.header("Physical Activity Level")
    PhysicalActivity = st.number_input("Physical Activity Level (30: minimum and 100: maximum):", min_value=30,
                                       max_value=100)

    # Stress Level
    st.header('Stress Level')
    stress = st.slider("Stress Level", min_value=2, max_value=9, value=5)

    # BMI Category
    st.header('BMI Category')
    BMI = st.radio("BMI Category",
                   ["Normal (18.5 - 24.9 kg/m²)", "Overweight (25.0 - 29.9 kg/m²)", 'Obese(30.0 kg/m² or higher)'])

    # Blood Pressure
    st.header('Blood Pressure')
    pressureHigh = st.slider('Systolic', min_value=90, max_value=180, value=120)
    pressureLow = st.slider('Diastolic', min_value=60, max_value=90, value=80)

    # Heart rate
    st.header('Heart rate')
    HeartRate = st.slider('Heart rate', min_value=60, max_value=90, value=72)

    # Daily Steps
    st.header('Daily Steps')
    steps = st.slider('Daily step', min_value=1000, max_value=8000, value=5000)

    # display data
    data_display(name, gender, age, Sleep_Duration, Sleep_Quality, PhysicalActivity, stress, BMI, HeartRate, steps,
                 pressureHigh, pressureLow, occupation)
    # FOR BMI

    if BMI == 'Normal (18.5 - 24.9 kg/m²)':
        BMI = 1
    elif BMI == 'Overweight (25.0 - 29.9 kg/m²)':
        BMI = 0
    else:
        BMI = 2

    # FOR GENDER
    if gender == "Male":
        gender = 0
    else:
        gender = 1

    st.button('Submit', on_click=data_entry)

    users_data.extend(
        [gender, age, Sleep_Duration, Sleep_Quality, PhysicalActivity, stress, BMI, HeartRate, steps, pressureHigh,
         pressureLow, occupation])

    occ = users_data.pop()
    occ_list = ["Doctor", "Software Engineer", "Lawyer", "Nurse", "Teacher"]

    items = encode_occ(occ, occ_list)
    users_data.extend(items)


def prediction_page():
    st.title("REPORT")
    name = st.session_state.name
    age = st.session_state.age
    gender = st.session_state.gender
    occupation = st.session_state.occupation
    Sleep_Duration = st.session_state.Sleep_Duration
    Sleep_Quality = st.session_state.Sleep_Quality
    PhysicalActivity = st.session_state.PhysicalActivity
    stress = st.session_state.stress
    BMI = st.session_state.bmi
    HeartRate = st.session_state.heartRate
    steps = st.session_state.steps
    pressureHigh = st.session_state.pressureH
    pressureLow = st.session_state.pressureL
    users_data = st.session_state.users_data

    col1, col2 = st.columns(2)
    with col1:

        st.write("Name:", name)
        st.write("Gender: ", gender)
        st.write("Age: ", age)
        st.write("Occupation: ", occupation)
        st.write("BMI Category: ", BMI)
        st.write("Blood Pressure: ", pressureHigh, '/', pressureLow)

    with col2:
        st.write("Sleep Duration: ", Sleep_Duration)
        st.write("Sleep Quality: ", Sleep_Quality)
        st.write("Physical Activity Level: ", PhysicalActivity)
        st.write('Stress Level: ', stress)
        st.write("Heart Rate: ", HeartRate)
        st.write("Daily Steps: ", steps)

    if users_data:
        # Load model
        with open("./stress_check", 'rb') as file:
            model_loaded = pk.load(file)
            check = model_loaded.predict(np.array(users_data).reshape(1, -1))

        if check == "Fit":
            st.image(new_fit)
            st.success("You don't have any sleep disorder.")
        elif check == "Sleep Apnea":
            st.image(new_apenea)
            st.error(f"You have {check[0]}. Consult a doctor.")
        else:
            st.image(new_insomnia)
            st.error(f"You have {check[0]}. Consult a doctor.")

    st.button('Back', on_click=back_page1)


def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'Input Page'

    if st.session_state.page == 'Input Page':
        input_page()
    elif st.session_state.page == 'Prediction Page':
        prediction_page()


if __name__ == "__main__":
    main()
