# Milestone 3 — Results, Outputs & Evaluation

This document summarizes sample generated outputs, evaluation metrics, and short analysis for Milestone 3 (Clinical text generation & ICD-10 prediction).

## Files used for examples

- Input files (example): `Milestone_3/data_input/patient1.json`, `patient2.json`, `sample_patient.json`
- Corresponding model outputs (example): `Milestone_3/model_output/P001_output.json`, `P002_output.json`, `P003_output.json`

## Quick summary of sample outputs

### P001 — Patient P001 (meningioma)
- ICD-10: D32.0 — Benign neoplasm of cerebral meninges
- Clinical note: MRI suggests a left frontal lobe meningioma. Patient presents with vision loss and headache; neurosurgery referral, ophthalmology and neurology consultations recommended. Follow-up MRI in 3–6 months if conservative management.

### P002 — Patient P002 (suspected heart failure)
- ICD-10: I50.9 — Heart failure, unspecified
- Clinical note: Imaging shows mild cardiomegaly with congestion and symptoms of chest pain and shortness of breath. Recommend echocardiogram, BNP testing, ECG, labs, and cardiology referral.

### P003 — Patient P003 (possible glioma)
- ICD-10: C71.2 — Malignant neoplasm of temporal lobe
- Clinical note: MRI indicates a temporal region glioma with severe headache and nausea. Recommended steps: neurosurgery, neuro-oncology, biopsy/pathology, baseline neuro exam, steroid therapy as needed.

## Evaluation methodology & metrics

- ICD-10 code agreement: manual comparison with expected provisional diagnoses in input samples.
- Clinical note quality: qualitative review assessing clarity, completeness, and medical relevance.
- Text similarity: SentenceTransformers (cosine similarity) between model notes and reference notes; example average similarity score seen in experiments: **0.62** (partial alignment with clinical references).

## Observations

- Model-generated notes are concise and clinically coherent for structured inputs.
- ICD-10 predictions match likely codes for the provided provisional diagnoses in the sample inputs used.
- Some outputs require manual verification and clinical review before being considered for real-world use.

## Reproducibility

To regenerate the outputs used in this document, run the notebook: `03_text_generation_pipeline.ipynb` and ensure the `Milestone_3/data_input/` folder contains the sample JSON files.

## Notes & next steps

- Add a small automated evaluation script to compute ICD-10 accuracy across a larger test set.
- Extend similarity testing to include additional reference notes to get more robust evaluation scores.

---

