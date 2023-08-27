# page1.py
import streamlit as st
if "shared" not in st.session_state:
   st.session_state["shared"] = True

# page2.py
import streamlit as st
st.write(st.session_state["shared"])
# If page1 already executed, this should write True