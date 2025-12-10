import os
import io
import json
import numpy as np
from PIL import Image
from dotenv import load_dotenv
import openai

load_dotenv()  
openai.api_key = os.getenv("OPENAI_API_KEY")

# Warn if API key missing but don't crash - image enhancement still works
if not openai.api_key:
    print("WARNING: OPENAI_API_KEY not found! Clinical note generation will not work.")
    print("Image enhancement will still work without the API key.")


import cv2

def enhance_image(image_bytes: bytes) -> bytes:
    """
    Input: raw image bytes
    Output: enhanced image bytes (CLAHE + sharpening)
    """
    try:
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            return image_bytes

        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        l = clahe.apply(l)
        lab = cv2.merge((l, a, b))
        enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        enhanced = cv2.filter2D(enhanced, -1, kernel)

        _, buffer = cv2.imencode('.png', enhanced)
        return buffer.tobytes()

    except Exception as e:
        print(f"Enhancement failed: {e}, returning original")
        return image_bytes

def generate_note(patient_data: dict) -> dict:
    # Check if API key is available
    if not openai.api_key:
        return {
            "note": "ERROR: OpenAI API key not configured. Please add OPENAI_API_KEY to your .env file.",
            "icd10": [{"code": "ERROR", "description": "API key missing"}]
        }
    
    prompt = f"""You are a senior neurologist writing a short, crisp OPD clinical note.

Patient: {patient_data.get('patient_name', 'Unknown')}, {patient_data.get('age', 50)}-year-old {patient_data.get('gender', 'Male')}
Chief Complaint: {patient_data.get('symptoms', patient_data.get('chief_complaint', 'Not provided'))}
MRI Brain: {patient_data.get('mri_findings', patient_data.get('observations', 'Not provided'))}
Provisional Diagnosis: {patient_data.get('provisional_diagnosis', patient_data.get('prelim_diagnosis', 'Not specified'))}

Write a concise, professional clinical note in 4–6 sentences only (exactly like Indian hospital OPD paper).
Then give ONLY ONE correct ICD-10 code.

Return ONLY this JSON:
{{
  "clinical_note": "short note here",
  "icd10_code": "",
  "icd10_description": ""
}}
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=800
        )
        raw = response.choices[0].message.content.strip()

        if "```json" in raw:
            raw = raw.split("```json")[1].split("```")[0]
        elif "```" in raw:
            raw = raw.split("```")[0].strip()

        data = json.loads(raw)  

        return {
            "note": data.get("clinical_note", "Note generation failed"),
            "icd10": [{
                "code": data.get("icd10_code", "Z03.8").strip().upper(),
                "description": data.get("icd10_description", "Unknown")
            }]
        }

    except json.JSONDecodeError:
        raw = raw.strip()
        if raw.count('"') % 2 != 0:
            raw += '"'
        if not raw.endswith('}'):
            raw += '}'
        try:
            data = json.loads(raw)
        except:
            data = {"clinical_note": raw[:1000], "icd10_code": "Z03.8", "icd10_description": "Observation"}
        return {
            "note": data.get("clinical_note", "Failed"),
            "icd10": [{"code": data.get("icd10_code", "Z03.8"), "description": data.get("icd10_description", "Error")}]
        }

    except Exception as e:
        return {
            "note": f"Error: {str(e)}",
            "icd10": [{"code": "ERROR", "description": str(e)}]
        }