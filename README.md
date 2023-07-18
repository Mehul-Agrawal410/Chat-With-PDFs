# Chat-With-PDFs

An interactive chatbot powered by OpenAI's GPT-3.5 model, designed to engage with multiple PDFs and extract knowledge through seamless question-answering.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Requirements](#requirements)
- [References](#references)

## Introduction

Chat-With-PDFs is an intelligent chatbot that leverages OpenAI's GPT-3.5 model to facilitate interactive conversations with multiple PDF documents. Users can effortlessly upload PDF files and ask questions related to the content of those documents. The chatbot utilizes cutting-edge language models to provide accurate and insightful responses, making it an efficient tool for knowledge extraction from PDFs.

## Getting Started

1. Install all the packages listed under Requirements
2. Create a `.env` file
3. Obtain an OpenAI API key and set it in the `.env` file as `OPENAI_API_KEY=your_api_key`
4. Run the application: `streamlit run app.py`

## Usage

1. A browser window should open after running the application.
2. Upload your PDF files by clicking on the "Browse files" button in the sidebar.
3. Click the "Submit" button to process the uploaded PDFs.
4. In the chat window, enter your questions related to the uploaded PDFs.
5. The chatbot, powered by OpenAI's GPT-3.5 model, will assist you by providing relevant answers and insights.

## Requirements

- Python 3.7+
- langchain
- streamlit
- streamlit-chat
- PyPDF2
- faiss-cpu
- openai
- tiktoken
- python-dotenv

## References

1. [Video Tutorial](https://youtu.be/dXxQ0LR-3Hg)
