import streamlit as st

# Initialize session state variables if they don't exist
if 'password' not in st.session_state:
    st.session_state["password"] = ''
if 'db_username' not in st.session_state:
    st.session_state["db_username"] = ''
if 'ind_name' not in st.session_state:
    st.session_state["ind_name"] = ''
if 'db_name' not in st.session_state:
    st.session_state["db_name"] = ''
if 'col_name' not in st.session_state:
    st.session_state["col_name"] = ''


st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <h1 style="margin-right: 10px; font-size: 45px;">CosmosDB Setup</h1>
        <img src="https://stormstatic.azureedge.net/storm/40e8fe02-8ebb-417f-2e05-08da06d53893/202309/azure-cosmos-db-featured.png" alt="CosmosDB Image" width="80">
    </div>
    """,
    unsafe_allow_html=True
)

st.write(" ## Please enter your CosmosDB connection string and collection details below.")
st.write("""
1. Go to your Azure portal and navigate to your CosmosDB account.
2. In the left-hand menu, select 'Connection String' under the 'Settings' section.
3. Copy the connection string provided.
4. Enter the connection string in the input box below.
5. Provide the database name and collection name where you want to upload the data.
""")

st.session_state.db_username = st.text_input("Username")
st.session_state.password = st.text_input("Password", type="password")
st.session_state.ind_name = st.text_input("Index Name")
st.session_state.db_name = st.text_input("Database Name")
st.session_state.col_name = st.text_input("Collection Name")

if st.button("Submit CosmosDB Config"):
    st.write("Username", st.session_state.db_username)
    st.write("Password", st.session_state.password)
    st.write("Index Name:", st.session_state.ind_name)
    st.write("Database Name:", st.session_state.db_name)
    st.write("Collection Name:", st.session_state.col_name)
