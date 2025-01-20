import streamlit as st

# Apply wide mode only for the first page
st.set_page_config(page_title="CosmosDB Data Uploader", page_icon=":rocket:", layout="wide")

mainpage = st.Page("content/home/CosmosDB-FileUploader.py", title="Main Page", default=True)
cosmosDBsetup = st.Page("content/settings/CosmosDB-Setup.py", title="CosmosDB Setup Page")
azureOpenAIsetup = st.Page("content/settings/AzureOpenAI-Setup.py", title="Azure OpenAI Setup Page")
fileUploader = st.Page("content/upload/File-Uploader.py", title="File Uploader Page")

pg = st.navigation(
    {
        "Home Page": [mainpage],
        "Setup": [cosmosDBsetup, azureOpenAIsetup],
        "File Uploader": [fileUploader]
    }
)
pg.run()