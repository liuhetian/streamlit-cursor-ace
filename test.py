import streamlit as st 
from streamlit_ace import st_ace

st.write("Hello World")
code = st_ace(auto_update=False)

code 

code2 = st_ace(auto_update=True)

code2

