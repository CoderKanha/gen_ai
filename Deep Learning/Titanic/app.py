import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model
import pickle

def survial_chance(result):
    if result > 0.5:
        return "Passanger will likely survive the Titanic Journey"
    else:
        return "Passanger will not likey survive the Titanic Journey"

st.title("Passenger Survival Chance in the Titanic Journey")

pclass = st.slider("Passenger Class", 1, 3)
sex = st.radio("Gender", ["male", "female"])
sibsp = st.slider("Sibling And Spouse count", 0, 10)
parch = st.slider("Parent and Child count", 0, 10)
fare = st.number_input("Fare")
embarked = st.radio("Gender", ["Chebourg", "Queenstown", "Southampton"]) 

data = pd.DataFrame([{
    "Pclass": pclass,
    "Sex": sex,
    "SibSp": sibsp,
    "Parch": parch,
    "Fare": fare,
    "Embarked": embarked
}])

with open("label_encoder.pkl", "rb") as file:
    label = pickle.load(file)

with open("one_hot_encoder.pkl", "rb") as file:
    onehot = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

model = load_model("model.h5")

data["Sex"] = label.transform(data["Sex"])
embarked = onehot.transform(data[["Embarked"]])

embarked = pd.DataFrame(embarked, columns=onehot.get_feature_names_out())

data = pd.concat([data.drop(columns=["Embarked"]), embarked], axis=1)

data[["Pclass", "SibSp", "Parch", "Fare"]] = scaler.transform(data[["Pclass", "SibSp", "Parch", "Fare"]])

y = model.predict(data)

result = y[0][0]

if st.button("Predict Survival"):
    st.write("Chances of Passenger Survival", (result*100).round(2),"%")
    st.write(survial_chance(result))