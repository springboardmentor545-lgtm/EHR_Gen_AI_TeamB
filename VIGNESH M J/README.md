# Milestone 4 — Frontend Development Contribution (Vignesh M J)

This document summarizes my **frontend contributions** for Milestone 4 of the project, "Enhancing EHRs with GenAI."

The goal of this milestone was to build a **fully interactive Streamlit-based frontend** that communicates with the FastAPI backend to deliver:

  * MRI image enhancement
  * Clinical text generation
  * ICD-10 prediction
  * Downloadable enhanced images
  * Display of model reasoning and medical recommendations

This milestone completes the **UI layer** of the system, providing a smooth and doctor-friendly workflow for interacting with the AI services.

-----

## Work Description (Frontend Only)

### Step 1 — Building the Streamlit UI Framework

I created a user-friendly Streamlit app with a modular file structure:

*Directory Structure (Simplified):*

```
frontend/
  ├─ app.py
  ├─ sections/
  │   ├─ image_enhancement.py
  │   ├─ clinical_notes.py
  │   └─ utils.py
  └─ assets/
```

**Key UI Functionalities Added:**

  * **Sidebar navigation** for easy switching between modules.
  * Clean layout using Streamlit containers, columns, and expanders.
  * Integrated **drag-and-drop uploader** for MRI scans.
  * **Real-time progress indicators** to manage user expectations.
  * Clear separation between the image enhancement and note-generation modules.

> This ensured the app was easy to use even for non-technical medical personnel.

-----

### Step 2 — Image Upload & Display Workflow

I implemented the complete workflow for the **MRI image enhancement** feature:

1.  **Upload:** User uploads MRI image (`jpg/png/dicom`).
2.  **Preview:** Original image is displayed in Streamlit.
3.  **Process:** Image bytes are sent to the backend via a `POST` request.
4.  **Output:** Enhanced image bytes are received and displayed.
5.  **Action:** A **download button** is provided for saving the result.

All network calls utilized the Python `requests` module with robust **exception-handling** to prevent UI crashes.

**Additional Features:**

  * File-type validation and error banners for incorrect formats.
  * **Loading spinners (`st.spinner`)** to show progress during long operations.
  * Optional image resizing before display to manage screen space.

-----

### Step 3 — Clinical Note & ICD-10 Generation UI

I built a complete **form-driven UI** for patient data input, designed to structure data for the LLM.

**Key Input Fields Included:**

  * Patient ID, Age, Gender
  * Symptoms, Medical history
  * Observations, Preliminary diagnosis

**After Submission, Output is Structured into Clean Display Sections:**

1.  Generated Clinical Note
2.  Predicted **ICD-10 Code & Description**
3.  Recommended Medical Steps
4.  Reasoning by LLM

> I used **expanders** to organize the output neatly and reduce clutter, improving scannability for the user.

-----

### Step 4 — Backend Integration & Error Handling

I established seamless integration with the FastAPI backend.

  * Implemented **reusable helper functions** for consistent API calls.
  * Added **retry logic** for handling temporary API timeouts.
  * Displayed **backend errors** directly in the UI with helpful, user-facing messages.
  * Constrained requests to avoid accidental **repeated submissions**.

> This ensures the frontend remains responsive and stable even under variable network conditions.

-----

### Step 5 — UI/UX Enhancements

To make the frontend more intuitive and visually appealing:

  * Used custom headings and colored text for emphasis.
  * Added **success banners (`st.success`)** upon successful completion.
  * Integrated **Streamlit cards-style layout** for results presentation.
  * Ensured images auto-fit container size for consistent layout.
  * Created a **consistent styling theme** across all pages.

> These improvements aligned the app with professional medical workflow tools.

-----

## Files Included (Frontend Only)

| File | Description |
| :--- | :--- |
| `app.py` | Main UI entry point (page switching, layout) |
| `sections/image_enhancement.py` | MRI enhancement UI workflow |
| `sections/clinical_notes.py` | Patient form & clinical note module |
| `sections/utils.py` | API calling utilities, validators |
| `assets/*` | Icons, sample images |

-----

## Tech Stack & Tools

  * **Streamlit** (Frontend framework)
  * **Python `requests`** (API communication)
  * **PIL** (Image handling)
  * **io / `base64`** (Image conversion utilities)
  * **FastAPI backend** (Integrated seamlessly)

The frontend was developed to communicate with the following backend endpoints:

  * `/enhance-image`
  * `/generate-note`

-----

## Challenges Faced

| Challenge | Solution |
| :--- | :--- |
| UI freezing during long enhancement operations | Solved using **loading spinners (`st.spinner`)** and asynchronous-like network handling to keep the UI responsive. |
| Enhanced image sometimes too large for display | Added **dynamic resizing** using PIL before displaying the image. |
| Streamlit caching interfering with repeated uploads | Implemented logic to **force-clear cache** on new uploads to ensure fresh processing. |
| JSON formatting from backend had edge cases | Added **safe JSON parsing** with `try-except` blocks and fallback rendering for text output. |

-----

## Summary

For Milestone 4, I developed a complete, fully functional ** BASIC Streamlit frontend** that:

  * Uploads and previews MRI images.
  * Sends data to the backend for enhancement.
  * Accepts structured patient details.
  * Generates clinical notes with ICD-10 prediction.
  * Shows reasoning and recommended steps.
  * Provides an **intuitive and stable user experience**.

This frontend ties all backend services together into a usable interface, **completing the multimodal EHR enhancement system.**
