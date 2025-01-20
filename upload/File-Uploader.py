import streamlit as st
import fitz
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores.azure_cosmos_db import (
    AzureCosmosDBVectorSearch,
    CosmosDBSimilarityType,
    CosmosDBVectorSearchType,
)
from langchain_openai import AzureOpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from pymongo import MongoClient
from langchain.schema import Document
from urllib.parse import quote_plus

st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <h1 style="margin-right: 10px; font-size: 45px;">File Upload 📂</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Please enter your CosmosDB connection string and collection details below.")

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

documents = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Read the PDF file
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        num_pages = pdf_document.page_count

        st.write(f"**{uploaded_file.name}**")
        
        # Collect text from all pages
        document_text = ""
        for page_num in range(num_pages):
            page = pdf_document.load_page(page_num)
            document_text += page.get_text()

        documents.append(document_text)

    # Split documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = []
    for uploaded_file, document_text in zip(uploaded_files, documents):
        for chunk in text_splitter.split_text(document_text):
            docs.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "file_name": uploaded_file.name
                    }
                )
            )

    st.write(docs)

    if st.button("Upload to CosmosDB"):
        azureopenai_embeddings = AzureOpenAIEmbeddings(
            api_key=st.session_state.api_key,
            azure_endpoint=st.session_state.api_endpoint,
            api_version=st.session_state.api_version,
            model=st.session_state.api_model_name,
            chunk_size=1
        )

        password = quote_plus(st.session_state.password)
        username = st.session_state.db_username
        con_string = f"mongodb+srv://{username}:{password}@clusterfortest1.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
        client: MongoClient = MongoClient(con_string)
        collection = client[st.session_state.db_name][st.session_state.col_name]

        vectorstore = AzureCosmosDBVectorSearch.from_documents(
            docs, 
            azureopenai_embeddings, 
            collection=collection, 
            index_name=st.session_state.ind_name)
        
        num_lists = 100
        dimensions = 1536
        similarity_algorithm = CosmosDBSimilarityType.COS
        kind = CosmosDBVectorSearchType.VECTOR_IVF
        m = 16
        ef_construction = 64
        ef_search = 40
        score_threshold = 0.1

        vectorstore.create_index(num_lists, dimensions, similarity_algorithm, kind, m, ef_construction)