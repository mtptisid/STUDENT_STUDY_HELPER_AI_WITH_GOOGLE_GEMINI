import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract text from PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=50000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create the FAISS vector store from text chunks using Gemini embeddings
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Function to set up the conversational chain with Gemini for answering questions
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not
    in the provided context just say, "answer is not available in the context", don't provide the wrong answer.\n\n
    Context:\n{context}?\n
    Question: \n{question}\n

    Answer:
    """

    # Using Gemini model for responses
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

# Function to process user input, search in FAISS index, and get a response from Gemini
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    try:
        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(user_question)

        chain = get_conversational_chain()
        
        response = chain(
            {"input_documents": docs, "question": user_question},
            return_only_outputs=True
        )

        st.write("Answer: ", response["output_text"])

    except Exception as e:
        st.error(f"Error occurred while processing the question: {str(e)}")

# Main function to render Streamlit UI
def main():
    st.set_page_config("Student Helping Chatbot", page_icon=":scroll:")
    st.header("Student Helper 🧑🏻‍🏫 - Chat Agent 👩🏻‍💻 ")

    user_question = st.text_input("Ask a Question from the Files uploaded ..  📂📑")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.image("img/Robot.jpg")
        st.title("📁 PDF File's Section")
        
        # File uploader for PDFs
        pdf_docs = st.file_uploader("Upload your Files", accept_multiple_files=True)
        
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Processing complete!")

        st.write("---")

    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0E1117; padding: 15px; text-align: center;">
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()