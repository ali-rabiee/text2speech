import streamlit as st
from gtts import gTTS
import os
from io import BytesIO
from PyPDF2 import PdfReader
import docx
from transformers import pipeline

# Initialize text_input
text_input = ''

# Initialize summarization pipeline
summarizer = pipeline('summarization', device=-1)

# Initialize session state for summarized text
if 'summarized_text' not in st.session_state:
    st.session_state.summarized_text = ''

# Streamlit app title
st.title('Text-to-Speech App')

# File uploader
uploaded_file = st.file_uploader('Upload a Word or PDF file', type=['docx', 'pdf'])

# Extract text from uploaded file
if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1]
    if file_type == 'docx':
        doc = docx.Document(uploaded_file)
        text_input = '\n'.join([para.text for para in doc.paragraphs])
    elif file_type == 'pdf':
        pdf_reader = PdfReader(uploaded_file)
        text_input = '\n'.join([page.extract_text() for page in pdf_reader.pages])
    else:
        st.error('Unsupported file type.')

# Text input area for manual input or extracted text
text_input = st.text_area('Enter text to convert to speech:', value=text_input)

# Button to generate speech from original text
if st.button('Generate Speech from Original Text'):
    if text_input:
        # Generate speech
        tts = gTTS(text_input)
        tts.save('output_original.mp3')
        
        # Provide download link
        st.audio('output_original.mp3', format='audio/mp3')
        st.success('Audio file from original text generated successfully!')
    else:
        st.error('Please enter some text.')

# Button to summarize text
if st.button('Summarize Text'):
    if text_input:
        # Summarize text
        summary = summarizer(text_input, max_length=130, min_length=30, do_sample=False)
        st.session_state.summarized_text = summary[0]['summary_text']
    else:
        st.error('Please enter some text or upload a file.')

# Display summarized text if available
if st.session_state.summarized_text:
    st.text_area('Summarized Text:', value=st.session_state.summarized_text, height=200)

    # Button to generate speech from summarized text
    if st.button('Generate Speech from Summarized Text'):
        # Generate speech
        tts = gTTS(st.session_state.summarized_text)
        tts.save('output_summarized.mp3')
        
        # Provide download link
        st.audio('output_summarized.mp3', format='audio/mp3')
        st.success('Audio file from summarized text generated successfully!')