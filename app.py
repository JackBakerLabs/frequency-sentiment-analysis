import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Basic Streamlit Template",
    page_icon=":rocket:",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("My Basic Streamlit App")

# File uploader
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])


if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)


# A simple button
if st.button("Click Me"):
    if uploaded_file:
        doshit()
    else:
        st.write("No File")
        