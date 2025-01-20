import os
import streamlit as st

st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <h1 style="margin-right: 10px; font-size: 45px;">CosmosDB Data Uploader 🛠️</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("""
# File Uploader for CosmosDB (MongoDB Vcore)

## Overview
Effortlessly upload and manage your files with our intuitive File Uploader for CosmosDB (MongoDB Vcore). Designed for seamless integration, this tool simplifies the process of transferring your data to your CosmosDB instance, ensuring efficiency and reliability.

## Key Features
- **User-Friendly Interface**: Navigate with ease through our clean and intuitive design.
- **Bulk Uploads**: Save time by uploading multiple files simultaneously.
- **Secure Transfers**: Ensure your data is protected with robust security protocols.
- **Real-Time Monitoring**: Track the progress of your uploads in real-time.
- **Error Handling**: Automatically detect and handle errors to ensure smooth uploads.
- **Compatibility**: Fully compatible with CosmosDB for MongoDB Vcore instances.
- **Vector Stores Creation**: Easily create vector stores to organize and manage your data.
- **Data Embedding**: Embed data into your indexes for enhanced search and retrieval capabilities.

## Why Choose Our Tool?
Our File Uploader is built with the user in mind, offering a hassle-free solution for managing your data uploads. Whether you're a developer, data analyst, or IT professional, our tool provides the functionality and reliability you need to keep your data organized and accessible.

## Get Started
Experience the convenience of seamless file uploads to your CosmosDB (MongoDB Vcore) instance.

## Setup Instructions
1. **CosmosDB Setup**: Enter your CosmosDB connection string and collection details (Side Panel).
2. **Azure OpenAI Setup**: Enter your Azure OpenAI API key, endpoint, API version, and model name (Side Panel).
3. **File Upload**: Upload your files to CosmosDB for MongoDB Vcore (Side Panel).
""")

