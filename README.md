# EHR_Gen_AI_TeamB

# AI-Powered-Enhanced EHR Imaging & Documentation System

## 📖 Project Overview

This project aims to revolutionize **Electronic Health Records (EHR)** by integrating **Generative AI (GenAI)** capabilities powered by **Azure OpenAI**. The system addresses two critical challenges in modern healthcare: the need for high-clarity medical imaging and the burden of administrative documentation.

By automating clinical notes, streamlining ICD-10 coding, and enhancing medical image resolution, this system empowers clinicians to spend less time on non-clinical tasks and more time on patient care.

### 🎯 Key Objectives
* **Enhance Medical Imaging:** Improve the clarity, resolution, and interpretability of X-rays, MRIs, CTs, and Ultrasounds.
* **Automate Documentation:** Reduce administrative workload by generating clinical notes from doctor observations.
* **Streamline Coding:** Automatically map clinical inputs to standard ICD-10 classifications.
* **Azure Integration:** Leverage enterprise-grade AI through Azure OpenAI for security and scalability.

---

## 🚀 Features & Modules

The project is divided into four core modules. 

### ✅ Module 1: Data Collection & Preprocessing
* **Data Ingestion:** Aggregation of medical imaging datasets (X-ray, MRI, CT, DXA) and unstructured EHR text.
* **Preprocessing Pipeline:** Cleaning, labeling, and standardization of data to ensure compatibility with GenAI models.
* **Privacy Compliance:** Anonymization of patient data prior to model training/tuning.

### ✅ Module 2: Medical Imaging Enhancement
* **GenAI Reconstruction:** Utilizes generative models to denoise and realistically reconstruct medical images.
* **Resolution Upscaling:** enhancing image quality to support more accurate diagnostic visualization.
* **Modality Support:** Verified support for various imaging modalities (MRI, CT, X-Ray).

### ✅ Module 3: Clinical Note & ICD-10 Automation
* **Note Generation:** Converts structured data and brief doctor observations into comprehensive, grammatically correct clinical notes.
* **Smart Coding:** Analyzes EHR input to automatically suggest accurate ICD-10 codes, reducing billing errors and manual lookup time.
* **Workflow integration:** Designed to minimize the "pajama time" clinicians spend documenting after hours.

### ✅ Module 4: Integration & Deployment
* **Hospital System Integration:** Connecting the AI models with live EHR interfaces.
* **Real-time Inference:** Deploying models for real-time clinical usage.
* **User Training:** Onboarding sessions for medical staff.

---

## 📅 Project Timeline & Milestones

| Milestone | Description | Status |
| :--- | :--- | :--- |
| **Milestone 1** | **Data Collection & Preprocessing:** Imaging/EHR sources prepared and labeled. | ✅ **Completed** |
| **Milestone 2** | **Imaging Enhancement:** GenAI models functional for diagnostics. | ✅ **Completed** |
| **Milestone 3** | **Documentation Automation:** Clinical notes & ICD-10 coding tested. | ✅ **Completed** |
| **Milestone 4** | **Deployment:** Full integration into hospital systems. | ✅ **Completed** |

---

## 🛠️ Tech Stack

* **Core AI Engine:** Azure OpenAI Service
* **Programming Language:** Python 3.9+
* **Machine Learning:** PyTorch / TensorFlow (for image models)
* **Data Handling:** Pandas, NumPy, DICOM libraries (pydicom)
* **Backend/API:** Flask / FastAPI (for serving model endpoints)

---
