import streamlit as st

def configure_cosmosdb():
    st.title("CosmosDB Setup")
    
    # Input fields for CosmosDB configuration
    endpoint = st.text_input("CosmosDB Endpoint")
    key = st.text_input("CosmosDB Key", type="password")
    database_name = st.text_input("Database Name")
    container_name = st.text_input("Container Name")
    
    if st.button("Save Configuration"):
        # Here you would typically save the configuration to a secure location
        st.success("CosmosDB configuration saved successfully!")

if __name__ == "__main__":
    configure_cosmosdb()