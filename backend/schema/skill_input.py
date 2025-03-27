from pydantic import BaseModel

class SkillInput(BaseModel):
    qualifications: str
