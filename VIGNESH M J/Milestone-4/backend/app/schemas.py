from pydantic import BaseModel

class NoteRequest(BaseModel):
    patient_id: str
    age: int
    gender: str
    chief_complaint: str
    history: str
    observations: str
    prelim_diagnosis: str

class NoteResponse(BaseModel):
    patient_id: str
    note: str
    icd10: list

class EnhanceResponse(BaseModel):
    enhanced_image_base64: str
    filename: str
    width: int
    height: int
