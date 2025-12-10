🧠 Milestone 3 — AI-Based Clinical Note Generation & ICD-10 Coding
AI-Powered Enhanced EHR Imaging & Documentation System
📌 Overview

Milestone 3 transforms structured patient data and MRI findings into AI-generated clinical notes and ICD-10 medical codes.
This milestone bridges imaging + documentation by producing realistic OPD-style notes, exporting them, and evaluating the results.

🎯 Objectives

Generate clinically meaningful notes from patient metadata

Predict ICD-10 diagnosis codes

Support LLM-based and offline mock generation modes

Evaluate ICD code correctness and note quality using BLEU

Export final results in JSON + Excel format

📁 Files Used

mapping.csv – Combined dataset from Milestone 1 & 2

Enhanced MRI images 

Milestone3.ipynb – Notebook for this milestone

📂 Files Generated (Milestone 3 Output)
| File                             | Description                                   |
| -------------------------------- | --------------------------------------------- |
| **INPUT_FOR_AI.json**            | Patient dataset prepared for AI input         |
| **INPUT_FOR_AI.csv**             | Same dataset in tabular format                |
| **FINAL_CLINICAL_NOTES.json**    | AI/Mock-generated clinical notes + ICD codes  |
| **FINAL_EVALUATION_REPORT.xlsx** | Evaluation metrics (ICD accuracy, BLEU score) |

🏗 Step-by-Step Workflow
1️⃣ Load Mapping File & Preview Images

The notebook loads mapping.csv and optionally previews enhanced MRI images to ensure correct dataset linkage.

2️⃣ Generate Patient Metadata for AI Input

For each selected sample (up to 15):

Assigns a synthetic patient name

Generates age, gender

Creates symptoms based on diagnosis type

Constructs radiology findings

Maps diagnosis to 3 main categories:

Malignant Tumor

Benign Tumor

No Tumor

This becomes the official input dataset for AI.

3️⃣ Clinical Note Generation (AI / Mock Mode)
Mock Generator (Default)

Works offline.
Creates:

Condition summary

Assessment + radiologist impression

Treatment recommendation

ICD-10 code

ICD-10 description

OpenAI Generator (Optional)

Uses GPT-4o-mini.
Outputs:

Short, formatted OPD-style note

One ICD-10 code

ICD-10 description

Fully JSON-based response

4️⃣ Evaluation Metrics
✔ ICD-10 Code Evaluation

Measured using:

Exact Match

Smart Match (allows related ICD code families like D32/D33)

Family-Safe Check (ensures code belongs to correct medical block)

✔ BLEU Score

Evaluates similarity between:

Generated notes

Ground truth summary (symptoms + diagnosis + MRI findings)

5️⃣ Export Final Reports
Final files include:
Patient details
Generated note
Predicted ICD-10 code
Accuracy flags
BLEU score

Saved as:
FINAL_CLINICAL_NOTES.json
FINAL_EVALUATION_REPORT.xlsx

Contributor: Pranjali Tanaji Jadhav
