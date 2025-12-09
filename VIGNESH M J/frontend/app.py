import streamlit as st
import requests
import json

st.title("EHR Assistant + Image Enhancement")

BASE_URL = "http://127.0.0.1:8000"

# -------------------------------
# IMAGE ENHANCEMENT
# -------------------------------
st.header("Enhance Image")

uploaded = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

if uploaded:
    if st.button("Enhance"):
        files = {"file": uploaded.getvalue()}  # MUST match FastAPI name

        res = requests.post(f"{BASE_URL}/enhance-image", files=files)

        if res.status_code == 200:
            st.image(res.content)
        else:
            st.error(f"Enhancement failed: {res.text}")


# -------------------------------
# NOTE GENERATION
# -------------------------------
st.header("Generate Clinical Note")

patient_id = st.text_input("Patient ID")
name = st.text_input("Name")
age = st.number_input("Age", 0, 120)
symptoms = st.text_area("Symptoms")
history = st.text_area("Medical History")

if st.button("Generate Note"):
    payload = {
        "patient_id": patient_id,
        "name": name,
        "age": age,
        "symptoms": symptoms,
        "history": history
    }

    res = requests.post(
        f"{BASE_URL}/generate-note",
        json=payload
    )

    if res.status_code == 200:
        st.json(res.json())
    else:
        st.error(f"Error: {res.text}")
