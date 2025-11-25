# Contribution for Module 3 (Clinical Note Generation & ICD-10 Coding)

## Overview
This folder contains my work for Module 3 of our project "Enhancing EHRs with GenAI".  
All code execution, synthetic note generation, OpenAI integration, ICD-10 evaluation, and BLEU scoring were performed using Google Colab.

---

## Datasets Used
Dataset: Brain Tumor MRI Mapping File  
Description: mapping_with_modality.csv used for linking image IDs to clinical text  
Purpose: Selected 15 patient cases for generating clinical notes + ICD-10 codes  

Dataset: EHR Clinical Notes (Raw Text)  
Description: Used only to extract demographic details (Age, Gender) whenever available  
Note: Fallback defaults applied for missing demographics  

---

## Work Description
### Tasks Completed
1. Colab Setup & Path Initialization  
   - Mounted Google Drive  
   - Created folder structure for /Clinical_Notes  
   - Loaded mapping file and verified enhanced image availability  

2. Patient Sampling & Demographic Extraction  
   - Randomly selected 15 patients from mapping file  
   - Loaded raw text notes (if available) to extract Age/Gender via regex  
   - Applied default values when missing  
   - Assigned realistic Indian patient names (male/female lists + surnames)  

3. Symptom & MRI Findings Generation (Based on Diagnosis)  
   - Used rule-based templates for Malignant Tumor, Benign Tumor, and No Tumor / Normal MRI  
   - Generated symptoms and radiology-style MRI findings using controlled templates  

4. Creation of Final AI Input File  
   - Prepared a clean structured dataset containing patient_id, patient_name, age, gender, symptoms, mri_findings, provisional_diagnosis  
   - Exported in two formats: INPUT_FOR_AI.json and INPUT_FOR_AI.csv  

5. Clinical Note Generation using OpenAI (GPT-4o-mini)  
   - Generated a short, crisp 4–6 sentence OPD-style clinical note + one correct ICD-10 code for each of the 15 patients  
   - Enforced strict JSON output format  
   - Cleaned malformed outputs and handled decoding issues safely  
   - Stored final results in FINAL_CLINICAL_NOTES.json  

6. ICD-10 Code Evaluation (Strict + Smart Scoring)  
   - Defined gold-standard codes: Malignant → C71.9 | Benign → D33.9 | No Tumor → Z03.8  
   - Implemented smart scoring (accepted D32.* as alternative for benign tumors)  
   - Ensured no clinically unsafe category outputs  
   - Generated exact accuracy, smart accuracy, and family safety metrics  
   - Exported full evaluation to FINAL_EVALUATION_REPORT.xlsx  

7. BLEU Score Evaluation (Medical Linguistic Quality)  
   - Computed BLEU-2 score using symptoms, MRI findings, and provisional diagnosis as reference  
   - Achieved human-level writing quality BLEU scores across all 15 cases  

---

## Files Included
File: 03_clinical_note_generation.ipynb  
Description: Google Colab notebook containing all code for patient sampling, prompt engineering, OpenAI calls, evaluation, and BLEU scoring  

File: INPUT_FOR_AI.json  
Description: Structured input data fed to the GPT model  

File: INPUT_FOR_AI.csv  
Description: Same input data in CSV format  

File: FINAL_CLINICAL_NOTES.json  
Description: AI-generated clinical notes + ICD-10 codes for 15 patients  

File: FINAL_EVALUATION_REPORT.xlsx  
Description: Complete ICD-10 accuracy evaluation + safety checks  

File: README.md  
Description: This file with my contribution details  

---

## Tools & Technologies
- Python  
- Pandas, Regex, JSON  
- OpenAI GPT-4o-mini  
- NLTK (for BLEU scoring)  
- Google Colab  
- openpyxl (Excel handling)  

---

## Contributor
Name: Afreen  
Milestone: 3 – Clinical Note Generation + ICD-10 Coding  
Project: Enhancing EHRs with GenAI (Team B)  
Repository Path: /backend/Afreen/milestone3/