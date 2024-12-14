# Student Helper Chatbot 🧑🏻‍🏫👩🏻‍💻

This repository provides a chatbot built using LangChain, Gemini LLM, and PDF processing to answer questions based on uploaded PDF documents. The chatbot is designed to help students by answering their queries from the context of the uploaded files.

## Features

- Upload multiple PDF files for processing.
- The system extracts text from the uploaded PDFs and splits it into chunks for efficient search.
- The chatbot uses the Google Gemini LLM for answering user queries.
- Text chunks are stored in a FAISS vector store for fast similarity search.
- A conversational agent is implemented to return context-based answers.
- Allows users to ask questions related to the content in the uploaded files.

## Requirements

Make sure you have the following dependencies installed:

- Python 3.x
- Streamlit
- LangChain
- PyPDF2
- google-generativeai
- FAISS
- dotenv
- Langchain-Google-GenAI (Google API integration)

You can install the required dependencies using:

...bash
pip install -r requirements.txt
...

## Setup

1. **Clone this repository**:
   
   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/mtptisid/STUDENT_STUDY_HELPER_AI_WITH_GOOGLE_GEMINI.git
   cd STUDENT_STUDY_HELPER_AI_WITH_GOOGLE_GEMINI
   ```

2. **Set up environment variables**:

   Create a `.env` file in the root directory and add your Google API key for the chatbot to work:

   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```

3. **Run the Streamlit app**:

   Start the Streamlit app by running the following command:

   ```bash
   streamlit run app.py
   ```

   This will launch the app, and you can access it at `http://localhost:8501/` in your browser.

## How It Works

1. **Uploading PDFs**:
   - You can upload one or more PDF files using the file upload section in the sidebar.
   
2. **Processing PDFs**:
   - After uploading the PDFs, click "Submit & Process" to extract and split the text into chunks.
   - The extracted text is then stored in a FAISS vector store for efficient querying.

3. **Asking Questions**:
   - You can type your question in the input field. The chatbot will search the vector store for relevant information and respond based on the context of the uploaded documents.

## File Structure
```
│
├── app.py                # Main Streamlit application file
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables for Google API key
├── faiss_index/          # FAISS index directory for storing text embeddings
└── img/                  # Images for the UI (e.g., robot image)
```

### app.py

The `app.py` file contains the main logic for the Streamlit app. It handles:

- PDF file uploads
- Text extraction from PDFs
- Text chunking and vector store creation
- User query processing and chatbot response generation using the Google Gemini LLM

Make sure to replace `your_google_api_key_here` with your actual Google API key.

## How to Use

1. **Upload PDF files**:
   - Click on the "Upload Files" button in the sidebar to upload one or more PDF files.

2. **Process the PDFs**:
   - After uploading, click on the "Submit & Process" button. The text from the PDFs will be extracted and chunked into smaller sections.

3. **Ask a question**:
   - In the main chat interface, enter your question in the input field. The chatbot will search for relevant information in the uploaded PDFs and return an answer based on the context.

4. **View the answer**:
   - The chatbot will display the answer based on the relevant PDF content or return a message saying that the answer is not available.

## Customization

- You can modify the `get_conversational_chain()` function in `app.py` to customize the conversational agent's behavior and response style.
- You can adjust the chunk size and overlap in the `get_text_chunks()` function to control how the text is split.
- The vector store is saved in the `faiss_index` folder. You can load or save it as needed to preserve the data.

## Screenshots

<img width="1440" alt="Screenshot 2024-12-14 at 5 20 47 PM" src="https://github.com/user-attachments/assets/f350a192-02c4-4e3a-9497-baabb7931827" />

<img width="1440" alt="Screenshot 2024-12-14 at 5 26 18 PM" src="https://github.com/user-attachments/assets/0f55616c-01e0-4313-a327-68428154659f" />

<img width="1440" alt="Screenshot 2024-12-14 at 5 25 56 PM" src="https://github.com/user-attachments/assets/cc00eb01-5432-433a-83fc-e7181fc26c58" />

<img width="1440" alt="Screenshot 2024-12-14 at 5 20 38 PM" src="https://github.com/user-attachments/assets/b98cffd5-39e3-4b64-a91e-fe1c1eff60da" />

## Acknowledgements

- This project uses [LangChain](https://www.langchain.com/) for building the conversational chain.
- [Google Gemini](https://developers.google.com/ai/generative) is used for generating responses.
- [PyPDF2](https://pythonhosted.org/PyPDF2/) is used for extracting text from PDFs.
- [FAISS](https://github.com/facebookresearch/faiss) is used for fast similarity search.
