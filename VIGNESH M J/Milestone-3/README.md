# Milestone 3 — Individual Contribution (Vignesh M J)

## Overview

This document summarizes my individual contribution for Milestone 3 of the project **"Enhancing EHRs with GenAI"**.

The primary objective of this milestone was to design and implement an AI-driven clinical note generation and ICD-10 code prediction pipeline using structured patient data. All work was performed using Python, the Google Gemini API, and medical text-processing techniques. This milestone builds on the work completed in Milestone 1 (data preparation) and Milestone 2 (image enhancement).

## Datasets Used

| Dataset | Description | Source |
|---|---|---|
| EHR Dataset | Structured patient information including age, gender, symptoms, MRI findings, diagnosis, and treatment details. Used as input for AI text generation. | Kaggle – EHR Dataset (Gaurav Srivastav) |
| Generated patient samples | Small set of synthetic patient JSON files created for testing the AI pipeline. | Created manually as part of preprocessing for Milestone 3 |
## Work description

### Step 1 — Input data preparation

I cleaned and structured patient records into a consistent JSON format. Each patient profile contains fields such as:

- `age`
- `gender`
- `symptoms`
- `scan_findings`
- `provisional_diagnosis`

Example input folder and files:

```
Milestone_3/data_input/
  ├─ patient1.json
  ├─ patient2.json
  └─ sample_patient.json
```

All input files were validated for correct JSON formatting and compatibility with the downstream model pipeline.

### Step 2 — Connecting to a language model

I selected **Google Gemini 2.5 Flash** for clinical text generation because it offers a good balance between speed, cost, and reasoning ability. The Gemini API key was configured and the official `google-generativeai` client was used from Python.

The model was used to generate:

- Clinical notes
- ICD-10 code predictions
- Human-readable reasoning and justification

This delivered a working AI-assisted diagnostic component for the pipeline.

### Step 3 — Structured model output

Model responses were cleaned and converted into structured JSON objects for reliable downstream use. A typical output structure looks like:

```json
{
  "patient_name": "Sample",
  "clinical_note": "...",
  "icd10_code": "C70.0",
  "reasoning": "...",
  "next_steps": "..."
}
```

All generated outputs were saved under `Milestone_3/generated_output/` and verified to be machine-readable for subsequent integration.

### Step 4 — Automated workflow pipeline

I implemented a Python pipeline that automates the following steps:

1. Read input patient JSON files
2. Send each record to the Gemini model for inference
3. Receive and validate the model response
4. Convert the response into structured JSON
5. Save outputs to disk

This pipeline supports batch processing of multiple patient files and will be extended for multimodal (image + text) prediction in Milestone 4.

### Step 5 — Evaluation and validation

Model performance was evaluated using three strategies:

- **ICD-10 accuracy check** — Compared predicted ICD-10 codes to known values in the dataset and performed manual verification on sample patients.
- **Clinical note quality** — Assessed generated notes for clarity, completeness, medical relevance, and alignment with provided symptoms and imaging findings.
- **Text similarity** — Used SentenceTransformers and cosine similarity to compare model-generated notes to human-written reference summaries. Average similarity score: **0.48**, indicating partial alignment with expected clinical structure.

## Files included

| File / Folder | Description |
|---|---|
| `03_text_generation_pipeline.ipynb` | Full pipeline for AI text generation and ICD-10 prediction |
| `data_input/` | JSON & CSV files containing test patient records |
| `model_output/` | AI-generated clinical notes and ICD-10 outputs |
| `milestone3_results.md` | Summary of generated outputs and evaluations |
| `README.md` | Documentation for Milestone 3 |
## Tools & technologies

- Python 3.13
- Google Gemini API (`gemini-2.5-flash`)
- `google-generativeai` Python client
- pandas / json for data handling
- SentenceTransformers for similarity scoring
- VS Code / Jupyter Notebook

## Challenges faced

- Gemini model errors due to an incorrect model name — fixed by using `gemini-2.5-flash`.
- Difficulty structuring long free-text outputs — addressed via regex-based cleaning and JSON templates.
- Model produced overly detailed reports at times — prompt engineering used to make output concise.
- Windows-based warnings when running large Hugging Face models — worked around by using Gemini to avoid heavy local models.

## Summary

Milestone 3 implemented a complete AI-based clinical text generation system that produces:

- Structured clinical notes
- ICD-10 code predictions
- Human-readable medical reasoning

Key outcomes:

- A fully automated Python pipeline for batch processing patient records
- High-quality clinical notes produced by Google Gemini
- Quantitative evaluation via text similarity and ICD-10 matching

This milestone completes the NLP portion of the project and prepares the groundwork for Milestone 4, where the system will incorporate multimodal inputs (image + text).