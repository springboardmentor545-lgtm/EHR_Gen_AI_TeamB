from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import base64

from .database import Base, engine, SessionLocal
from .models import User
from .schemas import UserCreate, UserLogin, NoteRequest
from .auth_utils import hash_password, verify_password, create_token
from .enhance import enhance_image_bytes
from .note_generator import generate_note_logic

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

# ---------------- AUTH -----------------
@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        return {"error": "User already exists"}

    new_user = User(username=user.username, password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    return {"message": "User registered"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password):
        return {"error": "Invalid username or password"}

    token = create_token({"sub": user.username})
    return {"token": token}

# ---------------- IMAGE ENHANCE -----------------
@app.post("/enhance-image")
async def enhance_image(file: UploadFile = File(...)):
    img_bytes = await file.read()
    enhanced = enhance_image_bytes(img_bytes)
    return {
        "enhanced_image_base64": base64.b64encode(enhanced).decode()
    }

# ---------------- NOTE GENERATE -----------------
@app.post("/generate-note")
def generate_note(req: NoteRequest):
    note, icd10 = generate_note_logic(req)
    return {
        "note": note,
        "icd10": icd10
    }
