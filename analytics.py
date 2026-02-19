import streamlit as st
from api import get_top_students


def render():
    st.header("Analytics")

    st.subheader("Top Students")

    if st.button("Show Top Students"):
        data = get_top_students()
        if not data:
            st.info("Top students list is empty. Pehle students ko skills ke sath assessment score assign karein.")
        else:
            st.dataframe(data)
