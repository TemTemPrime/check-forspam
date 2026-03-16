import streamlit as st
import pickle
import pandas as pd
import joblib 

@st.cache_resource
def load_model():
    model = joblib.load("email_spam_model_pkl")  
    return model
model = load_model()
st.title("email spam prediciton")
st.write("Insert email below")

email = st.text_input("Insert Email")


if st.button("predict"):
    if email.strip() == "":
        st.warning("Please enter an email message.")
    else:
        prediction = model.predict([email])[0]

        if prediction == 1:
            st.error("🚨 This email is SPAM")
        else:
            st.success("✅ This email is NOT Spam")