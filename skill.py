import streamlit as st
from api import get_skills, create_skills, assign_skill_to_student


def render():
    st.header("Skills")

    st.subheader("Add a New Skill")

    name = st.text_input("Skill Name")
    category = st.text_input("Category")

    if st.button("Add Skill"):
        status = create_skills(name, category)

        if status == 200 or status == 201:
            st.success("Skill added successfully!")
        else:
            st.error("Failed to add skill. Please try again.")

    st.divider()
    st.subheader("Assign Skill + Assessment Score")

    student_id = st.number_input("Student ID", min_value=1, step=1)
    skill_id = st.number_input("Skill ID", min_value=1, step=1)
    proficiency_level = st.number_input("Proficiency Level (1-5)", min_value=1, max_value=5, step=1)
    assessment_score = st.number_input("Assessment Score (0-100)", min_value=0, max_value=100, step=1)

    if st.button("Assign Skill To Student"):
        status_code, data = assign_skill_to_student(student_id, skill_id, proficiency_level, assessment_score)
        if status_code == 200 or status_code == 201:
            st.success(data.get("message", "Skill assigned successfully"))
        else:
            st.error(data.get("detail", "Failed to assign skill"))

    st.divider()
    st.subheader("All Skills")

    if st.button("Load Skills"):
        skills = get_skills()
        st.dataframe(skills)
