import streamlit as st
from page import student, skill, analytics

st.set_page_config(
    page_title="Student Skills Tracker",
    layout="wide"
)
st.title("Student Skills Tracker System")

page = st.sidebar.selectbox(
    "Select a page:",
    ["Students", "Skills", "Analytics"]
)

if page == "Students":
    student.render()
elif page == "Skills":
    skill.render()
elif page == "Analytics":
    analytics.render()
