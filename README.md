# Intelligent Query Retrieval System - Web Interface

This is a user-friendly web interface built with Streamlit for the Intelligent Query Retrieval System. It provides a clean and interactive way to query large documents by connecting to a powerful, LLM-powered backend API.

\<\!-- Optional: Add a screenshot of your running app --\>

## 🚀 Key Features

- **Interactive UI:** Allows users to input any public document URL (PDF, DOCX) and ask multiple questions in plain English.
- **Real-time Analysis:** Communicates securely with the backend API to process documents and retrieve accurate, context-aware answers.
- **Clear Results Display:** Presents the questions and their corresponding answers in a clean, easy-to-read format.
- **Secure Configuration:** Uses Streamlit's built-in secrets management to handle API credentials safely.
- **User-Friendly Design:** Includes loading spinners and clear error messages to provide a smooth user experience.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **API Communication:** Python Requests

## 📖 How to Use the Live Application

1.  Navigate to the deployed application URL.
2.  In the "Document URL" field, paste the public URL of the PDF or DOCX file you wish to analyze.
3.  In the "Questions" text area, type one or more questions, with each question on a new line.
4.  Click the "Get Answers" button.
5.  The application will show a loading spinner while it communicates with the backend. The results will be displayed on the page once the analysis is complete.

_For detailed information on the backend API, local setup, and the core RAG architecture, please refer to the [backend repository](https://github.com/arbin-mahato/Intelligent-Query-Retrieval-System.git)._
