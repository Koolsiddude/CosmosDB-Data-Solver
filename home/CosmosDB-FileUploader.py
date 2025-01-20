import streamlit as st

st.title("CosmosDB File Uploader")
st.write("Upload your files to CosmosDB.")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "json", "txt"])

if uploaded_file is not None:
    # Process the uploaded file
    st.success("File uploaded successfully!")