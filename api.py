import requests

BASE_URL = "http://127.0.0.1:8000"


def get_students():
    response = requests.get(f"{BASE_URL}/students/")
    response.raise_for_status()
    return response.json()


def create_student(name, age, email):
    payload = {
        "name": name,
        "age": int(age),
        "email": email,
    }
    response = requests.post(f"{BASE_URL}/students/", json=payload)
    return response.status_code


def get_skills():
    response = requests.get(f"{BASE_URL}/skills/")
    response.raise_for_status()
    return response.json()


def create_skills(name, category):
    payload = {
        "name": name,
        "category": category,
    }
    response = requests.post(f"{BASE_URL}/skills/", json=payload)
    return response.status_code


def assign_skill_to_student(student_id, skill_id, proficiency_level, assessment_score):
    payload = {
        "skill_id": int(skill_id),
        "proficiency_level": int(proficiency_level),
        "assessment_score": int(assessment_score),
    }
    response = requests.post(f"{BASE_URL}/students/{int(student_id)}/skills", json=payload)
    try:
        body = response.json()
    except ValueError:
        body = {"detail": response.text}
    return response.status_code, body


def get_top_students():
    response = requests.get(f"{BASE_URL}/analytics/top_students")
    response.raise_for_status()
    return response.json()
