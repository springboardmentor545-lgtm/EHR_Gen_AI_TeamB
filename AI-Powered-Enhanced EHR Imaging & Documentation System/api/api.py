from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
from utils import enhance_image, generate_note
import json

app = FastAPI(title="EHR GenAI API", version="1.0")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NoteRequest(BaseModel):
    patient_id: str
    age: int
    gender: str
    chief_complaint: str
    history: str = ""
    observations: str = ""
    prelim_diagnosis: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/enhance-image")
async def enhance_image_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    enhanced_bytes = enhance_image(image_bytes)
    b64 = base64.b64encode(enhanced_bytes).decode()
    return {"enhanced_image_base64": b64}

@app.post("/generate-note")
async def generate_note_endpoint(req: NoteRequest):
    patient_data = {
        "patient_name": req.patient_id,  
        "age": req.age,
        "gender": req.gender,
        "symptoms": req.chief_complaint + (" " + req.history if req.history else ""),
        "mri_findings": req.observations,
        "provisional_diagnosis": req.prelim_diagnosis
    }
    result = generate_note(patient_data)
    return {
        "patient_id": req.patient_id,
        "note": result["note"],
        "icd10": result["icd10"]
    }