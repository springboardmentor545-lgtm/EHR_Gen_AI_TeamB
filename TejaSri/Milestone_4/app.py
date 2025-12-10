#Milestone_4frontend/app.py
PROJECT_DIR = '/content/ehr-gemini'

# Create directories if they don’t exist
import os
os.makedirs(f"{PROJECT_DIR}/frontend", exist_ok=True)

# frontend/app.py
ui_code = '''
import streamlit as st, requests, base64, io
from PIL import Image

API_URL = "http://127.0.0.1:8000"

st.title("EHR GenAI with Gemini")

tab1, tab2 = st.tabs(["Enhance MRI", "Generate Note"])

with tab1:
    uploaded = st.file_uploader("Upload MRI Image", type=["png","jpg","jpeg"])
    if uploaded and st.button("Enhance"):
        r = requests.post(f"{API_URL}/enhance-image", files={"file": uploaded})
        if r.status_code == 200:
            b64 = r.json()['enhanced_image_base64']
            img = Image.open(io.BytesIO(base64.b64decode(b64)))
            st.image(img, caption="Enhanced MRI")
        else:
            st.error("Enhancement failed")

with tab2:
    with st.form("note_form"):
        pid = st.text_input("Patient ID")
        age = st.number_input("Age",1,120,50)
        gender = st.selectbox("Gender",["Male","Female"])
        cc = st.text_area("Chief Complaint")
        hist = st.text_area("History")
        obs = st.text_area("MRI Findings")
        diag = st.text_input("Provisional Diagnosis")
        if st.form_submit_button("Generate"):
            payload = {
                "patient_id": pid, "age": age, "gender": gender,
                "chief_complaint": cc, "history": hist,
                "observations": obs, "prelim_diagnosis": diag
            }
            r = requests.post(f"{API_URL}/generate-note", json=payload)
            if r.status_code == 200:
                data = r.json()
                st.success(data['note'])
                st.info("ICD-10: "+data['icd10'][0]['code'])
            else:
                st.error("Failed to generate note")
'''

# Write to file
open(f"{PROJECT_DIR}/frontend/app.py", "w").write(ui_code)

print("frontend/app.py created successfully!")
