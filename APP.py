import streamlit as st
from dotenv import load_dotenv
import os
import time
import warnings
import logging
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
warnings.filterwarnings("ignore", category=FutureWarning)
logging.getLogger("transformers").setLevel(logging.ERROR)
os.environ["USER_AGENT"] = "rag-app"
load_dotenv()
groq_api_key = st.secrets["GROQ_API_KEY"]
st.set_page_config(page_title="Dynamic RAG with Groq", layout="wide")
st.image("PragyanAI_Transperent.png")
st.title("Dynamic RAG with Groq, FAISS, and Llama3")
if "vector" not in st.session_state:
    st.session_state.vector = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

