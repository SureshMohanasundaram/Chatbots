import streamlit as st 
import asyncio

st.set_page_config(page_title="Enhanced PDFChat",layout="wide",initial_sidebar_state="expanded")

async def main():
    st.title("PDFChat: ")
    option=st.selectbox("Select Option",("PDF","Blog","Database"))
    
if __name__=="__main__":
    asyncio.run(main())
