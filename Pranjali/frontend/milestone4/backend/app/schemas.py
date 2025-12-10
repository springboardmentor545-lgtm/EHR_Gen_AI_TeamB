from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class NoteRequest(BaseModel):
    patient_id: str
    age: int
    gender: str
    chief_complaint: str
    history: str
    observations: str
    prelim_diagnosis: str
