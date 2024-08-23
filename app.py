import streamlit as st 
import asyncio

st.set_page_config(page_title="Enhanced PDFChat",layout="wide",initial_sidebar_state="expanded")

async def main():
    st.title("PDFChat: ")
<<<<<<< HEAD
    option=st.selectbox("Select Option",("PDF","Blogs","Database"))
=======
    option=st.selectbox("Select Option",("PDF","Database"))
>>>>>>> c29084e96579a8ab15e8a7a1f849e10359650224
    
if __name__=="__main__":
    asyncio.run(main())
