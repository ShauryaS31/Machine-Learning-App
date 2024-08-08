import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info("This is a app that builds the machine learning model!")

with st.expander("Data"): 
  st.write("**Raw Data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/palmer-penguins/master/data/penguins_cleaned.csv")
  df

  st.write("**X**")
  X = df.drop("species", axis =1)
  X

  st.write("**Y**")
  Y = df.species
  Y
with st.expander("Data Visualization"):
  st.scatter_chart(data=df, x="bill_length_mm",y="body_mass_g", color="species")

#Data PReperation
with st.sidebar:
  st.header("Input Features")
  #"species","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g",
  island = st.selectbox("Island",("Torgersen","Biscoe","Dream"))
  gender= st.selectbox("Gender", ("Male", "Female"))
  bill_length_mm = st.slider("Bill Length (mm)", 32.1,59.6,43.9)
