# Text-to-Speech App

This is a Streamlit-based web application that converts text to speech. It supports text extraction from uploaded Word and PDF files, manual text input, and text summarization using a machine learning model.

## Features

- **File Upload**: Upload Word (`.docx`) or PDF files to extract text.
- **Text Input**: Manually input text to convert to speech.
- **Text Summarization**: Summarize the input text using a pre-trained summarization model.
- **Text-to-Speech Conversion**: Convert both original and summarized text to speech and download the audio files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text2speech.git
   cd text2speech
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501` to access the app.

## Acknowledgments

- The app uses the [gTTS](https://pypi.org/project/gTTS/) library for text-to-speech conversion.
- Text summarization is powered by the [transformers](https://huggingface.co/transformers/) library.
