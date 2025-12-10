# frontend/app.py
import streamlit as st
import requests
import base64
import os
from auth import login, signup

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

# ---------------------------
# Glass-morphism CSS
# ---------------------------
st.set_page_config(page_title="EHR GenAI", layout="wide")
GLASS_CSS = """
<style>
body {
  background: linear-gradient(135deg, #0d1117 0%, #1a1c22 100%);
  font-family: "Inter", sans-serif;
  color: #e5e5e5;
}
.glass {
  background: rgba(0,0,0,0.6);  /* dark glass */
  backdrop-filter: blur(12px) saturate(120%);
  -webkit-backdrop-filter: blur(12px) saturate(120%);
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,0.15);
  padding: 20px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}
.header {
  display: flex;
  align-items: center;
  gap: 12px;
}
.small-muted { color: #c0c0c0; font-size: 0.9rem }
.kv { color:#ffffff; font-weight:600 }
.logo {
  width:48px; height:48px; border-radius:10px; 
  background: linear-gradient(135deg, #4f46e5, #06b6d4);
  display:inline-block;
}
.stButton>button {
  background-color: #4f46e5;
  color: #fff;
  border-radius: 8px;
  border: none;
  padding: 6px 12px;
  font-weight: 600;
}
.stButton>button:hover {
  background-color: #06b6d4;
  color: #fff;
}
input, textarea, select {
  background-color: rgba(255,255,255,0.1);
  color: #e5e5e5;
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 6px;
  padding: 4px 6px;
}
</style>
"""
st.markdown(GLASS_CSS, unsafe_allow_html=True)

# ---------------------------
# API Helpers
# ---------------------------
def api_signup(username, password):
    try:
        resp = requests.post(f"{API_URL}/signup", json={"username": username, "password": password})
        try:
            data = resp.json() if resp.text else {}
        except ValueError:
            data = {"error": "Invalid JSON response from server"}
        if resp.status_code == 200:
            return True, data
        return False, data
    except Exception as e:
        return False, {"error": str(e)}

def api_login(username, password):
    try:
        resp = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
        try:
            data = resp.json() if resp.text else {}
        except ValueError:
            data = {"error": "Invalid JSON response from server"}
        if resp.status_code == 200:
            return True, data
        return False, data
    except Exception as e:
        return False, {"error": str(e)}

def get_auth_headers() -> dict:
    token = st.session_state.get("jwt_token")
    if token:
        return {"Authorization": f"Bearer {token}"}
    return {}

# ---------------------------
# Session State Initialization
# ---------------------------
if "jwt_token" not in st.session_state:
    st.session_state.jwt_token = None
if "username" not in st.session_state:
    st.session_state.username = None

# ---------------------------
# Header
# ---------------------------
with st.container():
    st.markdown(
        '<div class="glass header">'
        '<div class="logo"></div>'
        '<div><h2 style="margin:0">AI-Powered EHR — Demo</h2>'
        '<div class="small-muted">Clinical note generation + image enhancement</div></div>'
        '</div>',
        unsafe_allow_html=True
    )

# ---------------------------
# Authentication UI
# ---------------------------
if not st.session_state.jwt_token:
    tab1, tab2 = st.tabs(["Login", "Signup"])

    # ---- Login ----
    with tab1:
        with st.form("login_form", clear_on_submit=False):
            st.markdown("<div class='glass'>", unsafe_allow_html=True)
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            st.markdown("</div>", unsafe_allow_html=True)

        if submit:
            success, res = api_login(u, p)
            if success and "token" in res:
                st.session_state.jwt_token = res["token"]
                st.session_state.username = u
                st.success("Login successful ✅")
                st.experimental_rerun = lambda: None  # placeholder for old code
            else:
                msg = res.get("error", "Login failed")
                st.error(f"Login failed: {msg}")

    # ---- Signup ----
    with tab2:
        with st.form("signup_form", clear_on_submit=False):
            st.markdown("<div class='glass'>", unsafe_allow_html=True)
            u2 = st.text_input("Choose username", key="su_user")
            p2 = st.text_input("Choose password", type="password", key="su_pass")
            submit2 = st.form_submit_button("Create account")
            st.markdown("</div>", unsafe_allow_html=True)

        if submit2:
            success, res = api_signup(u2, p2)
            if success:
                st.success("Account created. Now login.")
            else:
                st.error(f"Signup failed: {res.get('error', 'Unknown')}")

# ---------------------------
# Main App UI
# ---------------------------
else:
    st.markdown(f"<div style='margin-top:10px' class='small-muted'>Logged in as <span class='kv'>{st.session_state.username}</span></div>", unsafe_allow_html=True)
    cols = st.columns([2, 1])
    with cols[1]:
        if st.button("Logout"):
            st.session_state.jwt_token = None
            st.session_state.username = None
            st.success("Logged out")
            # No need for rerun, session_state change triggers it automatically

    left, right = st.columns([2, 1])

    # ---- Image Enhancement ----
    with left:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.subheader("📸 Image Enhancement")
        uploaded_file = st.file_uploader("Upload MRI/CT Image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            st.image(uploaded_file, caption="Original", width=350)
            if st.button("Enhance Image"):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    headers = get_auth_headers()
                    res = requests.post(f"{API_URL}/enhance-image", files=files, headers=headers, timeout=30)
                    if res.status_code == 200:
                        b64 = res.json().get("enhanced_image_base64")
                        if b64:
                            img = base64.b64decode(b64)
                            st.image(img, caption="Enhanced", width=350)
                        else:
                            st.error("No image returned")
                    elif res.status_code == 401:
                        st.error("Unauthorized — please login again.")
                    else:
                        st.error(f"Error: {res.status_code} {res.text}")
                except Exception as e:
                    st.error(f"Request failed: {e}")
        st.markdown("</div>", unsafe_allow_html=True)

    # ---- Clinical Note & ICD-10 ----
    st.markdown("<div style='margin-top:14px' class='glass'>", unsafe_allow_html=True)
    st.subheader("📝 Generate Clinical Note & ICD-10")
    with st.form("note_form"):
        patient_id = st.text_input("Patient ID", "P001")
        age = st.number_input("Age", 1, 120, 45)
        gender = st.selectbox("Gender", ["Male", "Female"])
        cc = st.text_input("Chief Complaint", "chest pain")
        history = st.text_area("History", "diabetic for 10 years")
        obs = st.text_area("Observations", "elevated heart rate")
        pdx = st.text_input("Preliminary Diagnosis", "suspected angina")
        submit_note = st.form_submit_button("Generate Note")
    if submit_note:
        payload = {
            "patient_id": patient_id,
            "age": age,
            "gender": gender,
            "chief_complaint": cc,
            "history": history,
            "observations": obs,
            "prelim_diagnosis": pdx
        }
        try:
            headers = get_auth_headers()
            res = requests.post(f"{API_URL}/generate-note", json=payload, headers=headers, timeout=30)
            if res.status_code == 200:
                out = res.json()
                st.subheader("Generated Clinical Note")
                st.write(out.get("note"))
                st.subheader("ICD-10 Codes")
                for it in out.get("icd10", []):
                    st.write(f"**{it.get('code')}** – {it.get('description')}")
            elif res.status_code == 401:
                st.error("Unauthorized — please login.")
            else:
                st.error(f"Error: {res.status_code} {res.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")
    st.markdown("</div>", unsafe_allow_html=True)

    # ---- Project Info ----
    with right:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.subheader("Project Info")
        st.write("- AI-Powered EHR imaging & documentation")
        st.write("- Backend: FastAPI (JWT-protected endpoints)")
        st.write("- Frontend: Streamlit demo with glass UI")
        st.write("- Tip: Use a valid account to access protected APIs")
        st.markdown("</div>", unsafe_allow_html=True)
