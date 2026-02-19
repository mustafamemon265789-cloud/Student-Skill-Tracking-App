class Student:
    def __init__(self, id: int, name: str, email: str, age: int):
        self.id = id
        self.student_id = id
        self.name = name
        self.email = email
        self.age = age


class Skills:
    def __init__(self, id: int, name: str, category: str):
        self.id = id
        self.name = name
        self.category = category


class StudentSkill:
    def __init__(self, student_id: int, skill_id: int, proficiency_level: int, assessment_score: int):
        if not 1 <= int(proficiency_level) <= 5:
            raise ValueError("Proficiency level must be between 1 and 5")
        if not 0 <= int(assessment_score) <= 100:
            raise ValueError("Assessment score must be between 0 and 100")

        self.student_id = student_id
        self.skill_id = skill_id
        self.proficiency_level = int(proficiency_level)
        self.assessment_score = int(assessment_score)
