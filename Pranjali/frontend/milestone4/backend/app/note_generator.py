import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_note_logic(req):
    """
    Generates a clinical note + ICD-10 code using OpenAI GPT model.
    """

    # ---- Step 1: Create the prompt ----
    prompt = f"""
You are a medical AI assistant. 
Generate:

1. A clear, concise clinical note.
2. Correct ICD-10 code(s) with explanation.

Patient Details:
- Patient ID: {req.patient_id}
- Age: {req.age}
- Gender: {req.gender}
- Chief Complaint: {req.chief_complaint}
- History: {req.history}
- Observations: {req.observations}
- Preliminary Diagnosis: {req.prelim_diagnosis}

Return output in this JSON format ONLY:
{{
  "note": "...",
  "icd10": [
      {{"code": "CODE", "description": "DESCRIPTION"}}
  ]
}}
"""


    # ---- Step 2: Call OpenAI API ----
    response = client.chat.completions.create(
        model="gpt-4o-mini",     # use any available model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    ai_output = response.choices[0].message.content

    # ---- Step 3: Parse response safely ----
    import json

    try:
        data = json.loads(ai_output)
    except:
        # fallback if model does not return perfect json
        data = {
            "note": ai_output,
            "icd10": [{"code": "R69", "description": "Unknown diagnosis"}]
        }

    return data["note"], data["icd10"]
