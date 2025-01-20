import streamlit as st

# Initialize session state variables if they don't exist
if 'api_key' not in st.session_state:
    st.session_state["api_key"] = ''
if 'api_endpoint' not in st.session_state:
    st.session_state["api_endpoint"] = ''
if 'api_version' not in st.session_state:
    st.session_state["api_version"] = ''
if 'api_model_name' not in st.session_state:
    st.session_state["api_model_name"] = ''

st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <h1 style="margin-right: 10px; font-size: 45px;">Azure OpenAI Setup</h1>
        <img src="https://ai.azure.com/assets/aistudio-af17733a.svg" alt="CosmosDB Image" width="80">
    </div>
    """,
    unsafe_allow_html=True
)

st.write("## Please enter your Azure OpenAI details below.")
st.write("""
1. Go to your Azure portal and navigate to your Azure OpenAI resource.
2. In the left-hand menu, select 'Keys and Endpoint' under the 'Resource Management' section.
3. Copy the API key provided.
4. Go to the 'Overview' section to find your endpoint URL.
5. Note down the API version you are using.
6. Go to the 'Models' section to find the model name you want to use.
7. Enter the API key, endpoint, API version, and model name in the input boxes below.
""")

# Input fields
st.session_state.api_key = st.text_input("Your Azure OpenAI API Key")
st.session_state.api_endpoint = st.text_input("Your Azure OpenAI Endpoint")
st.session_state.api_version = st.text_input("Your Azure OpenAI API Version" )
st.session_state.api_model_name = st.text_input("Your Azure OpenAI Model Name")

# Button to submit the config
if st.button("Submit Azure OpenAI Config"):
    st.write("API Key:", st.session_state.api_key)
    st.write("API Endpoint:", st.session_state.api_endpoint)
    st.write("API Version:", st.session_state.api_version)
    st.write("API Model Name:", st.session_state.api_model_name)