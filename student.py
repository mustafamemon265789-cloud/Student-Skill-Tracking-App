import streamlit as st
from api import create_student, get_students


def render():
    st.header("Students")

    st.subheader("Add a New Student")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    email = st.text_input("Email")

    if st.button("Add Student"):
        status_code = create_student(name, age, email)

        if status_code == 200 or status_code == 201:
            st.success("Student added successfully!")
        else:
            st.error("Failed to add student. Please try again.")

    st.divider()
    st.subheader("All Students")

    if st.button("Load Students"):
        students = get_students()
        st.dataframe(students)
