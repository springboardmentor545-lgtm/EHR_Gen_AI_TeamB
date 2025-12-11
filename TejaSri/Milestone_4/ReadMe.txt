Milestone 4 — Frontend Development Contribution

 Project: EHR Enhancement Using Generative AI (Gemini)
 Contributor: Tejasri Nakka

This final report outlines the complete frontend development contribution for Milestone 4. My objective was to architect and implement a production-grade, physician-centric User Interface (UI) using Streamlit. This UI (`frontend/app.py`) serves as the crucial connective layer, fully integrating the multimodal capabilities of the Gemini-powered backend with our project datasets.

My work transforms the core functionalities—MRI Image Enhancement and Clinical Documentation—into a unified, intuitive application.


 1. Source and Context Summary (Provided Input)

The following section summarizes the architectural and dataset specifics used as the foundation for this frontend development phase.

1.1. Core System Architecture

The frontend development was executed against the following final system structure:

 File Structure: 
ehr-gemini/
│
├── backend/
│   ├── api.py               FastAPI service for external requests
│   └── utils.py             Core LLM invocation (Gemini-Pro, Gemini-Pro JSON Mode, Gemini + OpenCV)
│
├── frontend/
│   └── app.py               Streamlit Application - Primary Contribution
│
└── data/
    ├── images_processed/    M1/M2 Preprocessed Data
    └── ehr_notes_processed/  M3 Synthetic Data (Source: mapping.csv)

 Backend Services: Image Enhancement uses Gemini + OpenCV, Clinical Note Generation uses Gemini-Pro, and ICD-10 Prediction uses Gemini-Pro JSON Mode.
 Frontend Design: Features include Streamlit tabs (Enhance / Note), Base64 image rendering, and processing of JSON-based LLM output.

1.2. Datasets Utilized

 Brain Tumor MRI Dataset (Kaggle): Approximately 7,000 PNG images, used for the image enhancement and rendering modules.
 Synthetic EHR Notes Dataset: Generated using `mapping.csv`, driving the structured input and expected output for the Clinical Note Generation module.

---

 2. Detailed Frontend Implementation (Tejasri Nakka's Contribution)

The following narrative details the implementation of the Streamlit application, focusing on the two primary user modules and the technical enhancements made for stability.

2.1. Project Architecture and Flow

The final system architecture establishes a clear separation of concerns, with the frontend residing primarily in `frontend/app.py`. The UI is organized into two primary, high-level tabs: "Enhance Image" and "Generate Clinical Note," ensuring a logical and intuitive user experience.

2.2. Module A: MRI Image Enhancement Workflow

This module implements the full multimodal submission lifecycle, coordinating image upload with the backend's Gemini-Vision pipeline.

A. Input and Request Transmission
The workflow begins with a robust drag-and-drop file uploader (`st.file_uploader`) for secure PNG/JPEG MRI scans. Once the file is selected, the application executes a synchronous `requests.post` call to the FastAPI endpoint (`/enhance-image`). This call efficiently packages the raw image data for processing by the Gemini-Vision + OpenCV pipeline.

B. Response Visualization and Handling
The backend returns the enhanced image as a Base64 string. The frontend is solely responsible for:
1.  Decoding the Base64 data.
2.  Rendering the image using PIL (Python Imaging Library) and `st.image()`.
3.  Displaying a clear visual comparison between the Original and the Enhanced scan.

To improve the User Experience (UX), Streamlit Spinners (`st.spinner()`) are strategically implemented to provide active, visual feedback during the latency associated with the backend's generative and computer vision processing.

2.3. Module B: Clinical Note Generation & ICD-10 Prediction

This module handles the structured text-to-text generation workflow for comprehensive clinical documentation.

A. Structured Data Collection and Payload
A detailed form is presented to the user, capturing critical patient data via dedicated input fields. This structure accurately mirrors a clinical review, collecting key data points such as: Patient Demographics, Chief Complaint, MRI Findings, and Provisional Diagnosis. This collected information is aggregated into a validated JSON object payload.

B. Request Transmission and Dual AI Invocation
The JSON payload is submitted to the `/generate-note` endpoint. This single request triggers two concurrent, specialized backend functions:
1.  Gemini-Pro is used for the complex task of synthesizing the full, narrative-style Clinical Note.
2.  Gemini-Pro JSON Mode is used specifically for the precise, structured output required for the ICD-10 Code and Description prediction.

C. Output Parsing and Presentation
The frontend receives the combined structured output. Robust Python logic is used to safely parse the returned data. The results are presented in a professional format: the extensive AI-Generated Clinical Note is rendered in a scrollable container, and the precise ICD-10 Code and Description are highlighted using Streamlit cards for immediate visibility.

---

 3. Robustness and Usability Enhancements

Key stability and usability features were implemented across the UI to ensure the application is reliable and ready for clinical use.

 Adaptive Image Resizing: The frontend utilizes the PIL library to dynamically constrain the display width of all rendered MRI images. This prevents UI overflow and maintains aesthetic consistency regardless of the original image resolution.
 Comprehensive Exception Handling: All critical API calls are wrapped in `try-except` blocks that issue specific `st.error()` messages. This guarantees a graceful failure mechanism, informing the user clearly of any backend or network issues.
 Safe LLM Output Handling: Custom parsing functions were developed to ensure the reliable extraction of data from the LLM responses. This included specialized logic to handle and mitigate potential formatting errors in Gemini's JSON output, guaranteeing accurate retrieval of the ICD-10 codes.

---

 4. Conclusion of Frontend Deliverables

My Milestone-4 contribution successfully deployed a fully featured, Streamlit-based interface that realizes the final phase of the EHR GenAI system. This frontend efficiently handles file upload (MRI), complex data structuring (Clinical Notes), safe API communication, and the structured visualization of Gemini's multimodal and generative outputs.

This work completes the visual and interactive layer, culminating in a functional, integrated AI assistant ready for comprehensive clinical demonstration.
