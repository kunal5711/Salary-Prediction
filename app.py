import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Salary_data.csv")

st.title("Salary Prediction")

nav = st.sidebar.selectbox("Navigation",["Home", "Prediction","Contribute"])

if nav == "Home":
    if st.checkbox("Show Data"):
        st.table(data)

    sel =  st.selectbox("How you want to see the data", ["Interactive", "Non-Interactive"])

    if sel == "Interactive":
        val = st.slider("How many years of data you want to see?", 0, 10, 1)
        df = data[data['YearsExperience'] <= val]
        fig, ax = plt.subplots()
        ax.scatter(df['YearsExperience'], df['Salary'])
        st.pyplot(fig)

    if sel == "Non-Interactive":
        fig, ax = plt.subplots()
        ax.plot(data['YearsExperience'], data['Salary'])
        st.pyplot(fig)

if nav == "Prediction":
    st.header("Predictor")

    lr = LinearRegression()
    x = np.array(data['YearsExperience']).reshape(-1,1)
    y = np.array(data['Salary']).reshape(-1,1)
    lr.fit(x, y)

    ex = st.number_input("Years of Experience", 0.00, 20.00)
    if st.button("Submit"):
        ex = np.array(ex).reshape(-1,1)
        salary = lr.predict(ex)
        st.success(f"Expected salary: {round(salary[0][0])}")

if nav == "Contribute":
    e = st.number_input("Years of Experience", 0.00, 20.00, 1.00)
    s = st.number_input("Your salary", 10000.00, 10000000.00)
    to_add = {"YearsExperience": e, "Salary": s}
    to_add = pd.DataFrame(to_add, index = [0])
    if st.button("Add"):
        to_add.to_csv("Salary_data.csv", mode = "a", index=False, header = False)
        st.success("Submitted successfully")