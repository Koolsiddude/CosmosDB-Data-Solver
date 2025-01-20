import streamlit as st

def azure_openai_setup():
    st.title("Azure OpenAI Setup")
    st.write("Configure your Azure OpenAI settings here.")

    api_key = st.text_input("API Key", type="password")
    endpoint = st.text_input("Endpoint URL")
    
    if st.button("Save Settings"):
        if api_key and endpoint:
            st.success("Azure OpenAI settings saved successfully!")
        else:
            st.error("Please fill in all fields.")