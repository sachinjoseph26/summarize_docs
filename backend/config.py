#import os
#from dotenv import load_dotenv
#
## Load environment variables
#load_dotenv()

#class Config:
#    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


import streamlit as st

class Config:
    # Load secrets from Streamlit Cloud
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]