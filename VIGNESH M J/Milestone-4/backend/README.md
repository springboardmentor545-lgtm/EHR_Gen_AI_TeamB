# Milestone 4 — Backend Development Contribution (Vignesh M J)

This document details my **backend-specific contributions** for Milestone 4 of the project, **"Enhancing EHRs with GenAI."**

The primary objective was to design and implement a **fully functional FastAPI backend** capable of handling:

  * **MRI image enhancement**
  * **Clinical note generation**
  * **ICD-10 prediction**
  * **Multimodal request handling**

The backend is the **core engine** powering the end-to-end system used by the frontend (Streamlit).

-----

## Work Description (Backend Only)

### Step 1 — Backend Architecture Setup

I established a **modular, clean backend structure** using **FastAPI**.

*Directory Structure (Simplified):*

```
backend/
  ├─ app/
  │   ├─ main.py
  │   ├─ enhance.py
  │   ├─ notes.py
  │   ├─ models.py
  │   ├─ utils/
  │   └─ data/
  └─ ...
```

**Key Features Added:**

  * **Organized modules** for clear separation of responsibilities (`enhance.py`, `notes.py`).
  * **Centralized routing** in `main.py`.
  * **Pydantic models** for robust request/response validation.
  * **CORS configuration** for secure communication with the Streamlit frontend.

-----

### Step 2 — Implementing Image Enhancement API

I implemented the `/enhance-image` endpoint, which handles **MRI image enhancement**.

**Key Backend Work:**

  * Accepts `UploadFile` containing the MRI image.
  * Handles file processing: **File → bytes → temporary file**.
  * Runs the **Real-ESRGAN executable** using the `subprocess` module.
  * Loads the enhanced image bytes and returns them as a **FastAPI `StreamingResponse`**.
  * **Crucially:** Ensures proper disposal of temporary files to prevent memory leaks.

> The function guarantees stable enhancement execution and correct image format handling (mostly PNG) for Streamlit UI compatibility.

-----

### Step 3 — Implementing Clinical Note Generation API

The `/generate-note` endpoint processes patient data and generates four key pieces of information: **Clinical note, ICD-10 code, Medical reasoning,** and **Suggested next steps.**

**Backend Achievements:**

  * Integrated the **Gemini 2.5 Flash** model for medical text generation.
  * Defined **`NoteRequest`** and **`NoteResponse`** Pydantic schemas.
  * Created a robust **parsing method** to extract structured **JSON** from the model's text output.
  * Implemented **fallback error-handling** if the Gemini output is malformed (non-JSON).

> The output is guaranteed to be clean, consistent, **JSON-valid**, and Streamlit-compatible.

-----

### Step 4 — Data Processing & Validation Layer

I added multiple preprocessing and post-processing steps to ensure data integrity and consistency.

  * **Input Validation:** All input fields are validated using **Pydantic** before hitting the model.
  * **Graceful Handling:** Missing or empty values are handled gracefully.
  * **Output Cleaning:** Output texts are cleaned (**removed unwanted characters, newlines, or model hallucinations**).
  * **ICD-10 Cross-check:** Generated ICD-10 codes are validated against the internal lookup table (`data/icd_lookup.csv`).

> These validations prevent backend crashes and significantly improve response consistency and quality.

-----

### Step 5 — Testing & Debugging the Backend

I performed extensive backend testing to ensure reliability.

#### Functional Testing

  * Verified both endpoints independently using the **/docs (Swagger UI)**.
  * Ensured correct image processing and structured JSON response generation.

#### Error Handling Tests

  * Tested **invalid image formats** and **large input files**.
  * Verified handling of **invalid JSON keys** in requests.
  * Validated robustness against **Network/API timeouts** from the Gemini service.

#### Performance Testing

  * Measured enhancement latency **(\~1–3 sec)**.
  * Verified **stable API uptime** over repeated calls.

-----

## Files Included (Backend Only)

| File | Purpose |
| :--- | :--- |
| `app/main.py` | Routes, API initialization, **CORS setup** |
| `app/enhance.py` | Image enhancement engine (**Real-ESRGAN wrapper**) |
| `app/notes.py` | Clinical note + ICD-10 generator (**Gemini integration**) |
| `app/models.py` | **Pydantic** request/response schemas |
| `data/icd_lookup.csv` | Internal ICD-10 lookup file |
| `app/utils/*.py` | Helper functions for cleaning & validation |

-----

## Tools & Technologies

  * **FastAPI** (Core backend framework)
  * **Uvicorn** (Local API server)
  * **Real-ESRGAN NCNN Vulkan** (MRI enhancement engine)
  * **Google Gemini API** (Clinical note + ICD-10 generation)
  * **Pydantic** (Request/response validation)
  * **Pillow, subprocess, io, tempfile** (Core Python libraries)

-----

## Challenges Faced (Backend Focused)

| Challenge | Solution |
| :--- | :--- |
| `FileNotFound` error for ICD lookup file | Fixed by correcting relative paths and ensuring the CSV was in the right directory (`data/`). |
| `Subprocess` failures while running Real-ESRGAN | Resolved by validating executable paths and using safer, system-guaranteed temporary files. |
| Gemini returning non-JSON text | Solved using **strict prompting** and a **regex-based cleanup/parsing** method for robust JSON extraction. |
| CORS errors during Streamlit integration | Fixed using the standard **FastAPI middleware** for CORS configuration. |

-----

## Summary

My backend contributions for Milestone 4 successfully delivered:

  * A **fast, stable, and clean FastAPI service**.
  * A fully functional **image enhancement API**.
  * A reliable **clinical note + ICD-10 prediction API**.
  * **Strong validation and error handling** throughout the pipeline.
  * **Smooth integration** with the Streamlit UI.

This backend serves as the **core engine** of our multimodal EHR enhancement system and successfully integrates all work done in Milestones 1–3.