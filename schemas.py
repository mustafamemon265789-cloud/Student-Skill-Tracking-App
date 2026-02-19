from pydantic import BaseModel, Field
from typing import Optional

class StudentBase(BaseModel):
    name : str
    email : str
    age :int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name : Optional[str] = None
    email : Optional[str] = None
    age : Optional[int] = None

class StudentResponse(StudentBase):
    id : int
    name : str
    email : str
    age : int

class SkillCreate(BaseModel):
    name:str
    category:str

class SkillResponse(BaseModel):
    id:int
    name:str
    category:str

class StudentSkillCreate(BaseModel):
    skill_id: int
    proficiency_level:int
    assessment_score:int