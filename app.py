import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from streamlit_chat import message

def get_text(docs):
    text = ''
    for doc in docs:
        pdf_reader = PdfReader(doc)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_chunks(text):
    splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200, length_function = len)
    chunks = splitter.split_text(text)
    return chunks

def get_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embeddings)
    return vectorstore

def get_chat_chain(vectorstore):
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    chat_chain = ConversationalRetrievalChain.from_llm(ChatOpenAI(), vectorstore.as_retriever(),memory = memory)
    return chat_chain

def handleQuery(query):
    res = st.session_state.chat({'question': query})
    st.session_state.history = res['chat_history']
    for i, msg in enumerate(st.session_state.history):
        if i % 2 == 0:
            message(msg.content, is_user=True, avatar_style='miniavs', seed=8)
        else:
            message(msg.content)
def main():
    load_dotenv()
    st.set_page_config(page_title='Multi Pdf Chatbot', page_icon=':robot_face:')

    st.header('Multi Pdf Chatbot :books:')
    query = st.text_input('Enter your query:')
    if query:
        handleQuery(query)


    with st.sidebar:
        st.subheader('Uploaded documents')
        docs = st.file_uploader('Upload PDFs', type=['pdf'], accept_multiple_files=True)
        if st.button('Submit'):
            with st.spinner('Processing'):
                raw_text = get_text(docs)
                chunks = get_chunks(raw_text)
                vectorstore = get_vectorstore(chunks)
                st.session_state.chat = get_chat_chain(vectorstore)
if __name__ == '__main__':
    main()