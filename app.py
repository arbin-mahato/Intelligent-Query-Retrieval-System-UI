# app.py - A Streamlit UI for the Intelligent Document Query System

import streamlit as st
import requests
import json

# --- CONFIGURATION (SECURE METHOD) ---
try:
    API_ENDPOINT = st.secrets["API_ENDPOINT"]
    BEARER_TOKEN = st.secrets["BEARER_TOKEN"]
except KeyError:
    st.error("ERROR: API_ENDPOINT and BEARER_TOKEN secrets are not set.")
    st.stop()


# --- PAGE SETUP ---
st.set_page_config(
    page_title="Intelligent Query Retrieval System",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- UI COMPONENTS ---
st.title("🤖 Intelligent Query Retrieval System")
st.write(
    "This interface allows you to ask questions about a document hosted online. "
    "Provide the document's URL and your questions below to get started."
)

# --- INPUT FORM ---
with st.form("query_form"):
    doc_url = st.text_input(
        "Document URL",
        value="https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
        placeholder="https://.../policy.pdf",
        help="Enter the public URL of the PDF or DOCX file you want to query."
    )

    questions_text = st.text_area(
        "Questions (one per line)",
        height=150,
        placeholder="What is the grace period for premium payment?\nWhat is the waiting period for cataract surgery?",
        help="Enter each question on a new line."
    )

    submitted = st.form_submit_button("Get Answers", type="primary")

# --- API CALL AND RESULT DISPLAY ---
if submitted:
    # Validate inputs
    if not doc_url or not questions_text:
        st.error("Please provide both a document URL and at least one question.")
    else:
        # Prepare data for the API call
        questions_list = [q.strip() for q in questions_text.split('\n') if q.strip()]
        
        if not questions_list:
            st.error("Please enter at least one valid question.")
        else:
            payload = {
                "documents": doc_url,
                "questions": questions_list
            }
            
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {BEARER_TOKEN}'
            }

            # Show a spinner while processing
            with st.spinner("Analyzing document and finding answers... This may take a moment for new documents."):
                try:
                    # Make the POST request to the deployed API
                    response = requests.post(API_ENDPOINT, headers=headers, json=payload, timeout=60)

                    # Check for a successful response
                    if response.status_code == 200:
                        results = response.json()
                        answers = results.get("answers", [])
                        
                        st.success("Analysis complete! Here are the answers:")
                        
                        # Display results in a clean format
                        for i, question in enumerate(questions_list):
                            with st.container(border=True):
                                st.markdown(f"**Q: {question}**")
                                st.write(f"A: {answers[i] if i < len(answers) else 'No answer provided.'}")
                    else:
                        # Handle API errors
                        error_data = response.json()
                        st.error(f"API Error (Status {response.status_code}): {error_data.get('detail', 'An unknown error occurred.')}")

                except requests.exceptions.RequestException as e:
                    # Handle network or connection errors
                    st.error(f"Failed to connect to the API. Please check the endpoint URL and your connection. Error: {e}")

# --- FOOTER ---
st.markdown("---")
st.write("Powered by an advanced RAG pipeline.")
