import streamlit as st
import pickle
import numpy as np


def load_model(model_name):
    with open(f'{model_name}.pkl', 'rb') as file:
        print("a",file)
        data = pickle.load(file)
    return data


def show_predict_page():
    st.write("""### We need some information to predict""")

    model_names = ['Logistic_Regression', 'KNN', 'Decision_Tree', 'Naive_Bayes']
    selected_model_name = st.selectbox('Model', model_names)

    # Load the selected model
    model = load_model(selected_model_name)

    EDMin = st.slider("Minimum Estimated Diameter in Kilometres", 0, 50, 2)
    EDMax = st.slider("Maximum Estimated Diameter in Kilometres", 0, 100, 10)
    RV = st.slider("Velocity Relative to Earth", 200, 250000, 10000)
    MD = st.slider("Distance in Kilometres missed", 6800, 75000000, 42618528)
    AM = st.slider("Describes intrinsic luminosity", 5, 35, 20)

    ok = st.button("Predict")

    if ok:
        x = np.array([[EDMin, EDMax, RV, MD, AM]]).reshape(1, -1)
        hazardous = model.predict(x)

        if hazardous == 0:
            st.subheader(f"The Potentially Non-Hazardous Asteroid")
        else:
            st.subheader(f"The Potentially Hazardous Asteroid")


