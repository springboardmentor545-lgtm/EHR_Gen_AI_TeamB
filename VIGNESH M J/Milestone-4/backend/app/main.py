from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from app.enhance import enhance_image_local
from app.notes import generate_note

from pydantic import BaseModel

app = FastAPI(title="EHR + Image Enhancement API")

class NoteRequest(BaseModel):
    patient_id: str
    name: str
    age: int
    symptoms: str
    history: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/enhance-image")
async def enhance_image_api(file: UploadFile = File(...)):
    img_bytes = await file.read()
    enhanced = enhance_image_local(img_bytes)
    return Response(content=enhanced, media_type="image/png")

@app.post("/generate-note")
def generate_note_api(payload: NoteRequest):
    result = generate_note(payload.dict())
    return result
