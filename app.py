import streamlit as st 
import asyncio

st.set_page_config(page_title="Enhanced PDFChat",layout="wide",initial_sidebar_state="expanded")

async def main():
    st.title("PDFChat: ")
    
    option=st.selectbox("Select Option",("PDF","Database"))
    
    if option == "PDF":
        uploaded_file = st.file_uploader("Choose a file",type="PDF")
        if uploaded_file is not None:
            with st.spinner("Processing..."):
                uploaded_file.seek(0)
                file = uploaded_file.read()
            
            st.session_state["ready"] = True
    
    
    elif option == "Database":
        uploaded_file = st.file_uploader("Choose a Database file",type="db")
        if uploaded_file is not None:
            with st.spinner("Processing..."):
                uploaded_file.seek(0)
                file = uploaded_file.read()
            
            st.session_state["ready"] = True
    
    if st.session_state.get("ready",False):
        if 'generated' not in st.session_state:
            st.session_state['generated'] = ["Welcome! you can ask any questions"]
            
        if 'past' not in st.session_state:
            st.session_state['past'] = ["Hey"]
            
        container = st.container()
        response_container = st.container()
        
        with container:
            with st.form(key='my_form',clear_on_submit=True):
                user_input = st.text_input("Query:",placeholder="e.g.Summarize the document",key='input')
                submit_button = st.form_submit_button(label="Send")

    
if __name__=="__main__":
    asyncio.run(main())
