import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


# Dictionary to map company names to pickle file paths
company_model_files = {
    "Apple": r"C:\Users\KISHORE\Desktop\FAANG\apple_best_model.pkl",
    "Google": r"C:\Users\KISHORE\Desktop\FAANG\google_bes_model.pkl",
    "Facebook": r"C:\Users\KISHORE\Desktop\FAANG\facebook_best_model.pkl",
    "Amazon": r"C:\Users\KISHORE\Desktop\FAANG\amazon_best_model.pkl",
    "Netflix": r"C:\Users\KISHORE\Desktop\FAANG\netflix_best_model.pkl"
}


st.markdown("---")
img_path = r"C:\Users\KISHORE\Desktop\FAANG\stockpic.jpeg"
st.image(img_path,width=1500)
st.markdown("---")
st.title("STOCK PRICE PREDICTION ")
st.write("by KISHORE KUMAR B N")
st.markdown("*****")
st.write("📊 📈 💹 💵 💰")


st.sidebar.header("Select the Company")
company = st.sidebar.selectbox(
    "Choose a company:",
    options=["Apple", "Google", "Facebook", "Amazon", "Netflix"]
    )

st.write(f"You selected: **{company}**")

model_path = company_model_files[company]
with open(model_path, "rb") as file:
    model = pickle.load(file)

with open(r"C:\Users\KISHORE\Desktop\FAANG\scalermodel.pkl", "rb") as file:
    scaler_model = pickle.load(file)

st.write(f"Loaded model for **{company}** successfully!")
    
st.header("Enter Feature Values")
feature_1 = st.number_input("Open", value=0.0)
feature_2 = st.number_input("High", value=0.0)
feature_3 = st.number_input("Low", value=0.0)
feature_4 = st.number_input("Volme", value=0.0)

user_input = np.array([[feature_1, feature_2, feature_3, feature_4]])
scaled_values=scaler_model.transform(user_input)

if st.button("Predict"):
    prediction = model.predict(scaled_values)
    st.success(f"The predicted Close price is: {prediction}")
