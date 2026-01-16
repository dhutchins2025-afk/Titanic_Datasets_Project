%%writefile app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = sns.load_dataset('titanic')

st.title("🚢 Titanic EDA App")

# Sidebar
st.sidebar.header("Settings")
gender = st.sidebar.selectbox("Select Gender", ["all", "male", "female"])

if gender != "all":
    df = df[df['sex'] == gender]

# Plot
st.subheader(f"Survival Count for {gender}")
fig, ax = plt.subplots()
sns.countplot(data=df, x='survived', palette='viridis', ax=ax)
st.pyplot(fig)
