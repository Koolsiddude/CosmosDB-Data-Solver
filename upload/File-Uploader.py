import streamlit as st

def upload_file():
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "json", "txt"])
    if uploaded_file is not None:
        # Process the uploaded file
        file_details = {
            "Filename": uploaded_file.name,
            "FileType": uploaded_file.type,
            "FileSize": uploaded_file.size
        }
        st.write(file_details)
        # Here you can add code to interact with CosmosDB and upload the file

def main():
    st.title("File Uploader")
    upload_file()

if __name__ == "__main__":
    main()