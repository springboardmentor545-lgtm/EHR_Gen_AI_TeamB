# Milestone 1 – Individual Contribution (Vignesh M J)

## Overview

This document summarizes my individual contribution for **Milestone 1** of the project *“Enhancing EHRs with GenAI.”*
All preprocessing, dataset integration, and analysis tasks were performed locally using **Python (Jupyter Notebook and VS Code)**.
The main objective was to collect, clean, and link **Electronic Health Record (EHR) data** with **medical imaging data** while establishing proper ICD-10 code mappings to enable downstream AI model training.

---

## Datasets Used

| Dataset                    | Description                                                                                                                   | Source                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **EHR Dataset**            | A synthetic dataset containing anonymized patient medical records, including tumor type, treatment, and survival information. | [Kaggle – EHR Dataset (Gaurav Srivastav)](https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset)                 |
| **Brain Tumor MRI Images** | Medical imaging dataset containing MRI scans of different brain tumor types used for image–EHR linking and classification.    | [Kaggle – Brain Tumors Dataset (Mohammad Hossein)](https://www.kaggle.com/datasets/mohammadhossein77/brain-tumors-dataset) |

---

## Work Description

### Tasks Completed

**1. Dataset Setup and Folder Structuring**

* Created a standardized project directory named `Enhancing_EHRs_with_GenAI/` with subfolders for raw, processed, and documentation files.
* Organized the data pipeline under `/data/raw`, `/data/images_processed`, and `/data/ehr_notes_processed`.

**2. Image Preprocessing**

* Processed MRI brain tumor images (glioma, meningioma, pituitary, notumor).
* Converted all images to grayscale and resized them to **256 × 256 pixels**.
* Used Python’s **PIL** library for conversion and normalization.
* Saved preprocessed images in `data/images_processed/`.

**3. EHR Cleaning and Normalization**

* Cleaned the Kaggle EHR dataset by removing missing and duplicate records.
* Standardized column names and string formats (lowercase, trimmed spaces).
* Saved the cleaned dataset in `ehr_notes_processed/cleaned_ehr.csv`.

**4. ICD-10 Code Mapping**

* Created a reference file `icd_lookup.csv` containing mappings between tumor types and ICD-10 codes.
* Implemented automated matching to assign ICD-10 codes for each record.
* Verified correctness of codes using a regular expression pattern check.

**5. Linking EHR and Imaging Data**

* Integrated cleaned EHR data with corresponding tumor-type images.
* Generated a unified dataset (`linked_brain_ehr.csv`) containing:
  `file_id, image_path, ehr_path, diagnosis, icd10_code, patient_id, age, gender, tumor_size(cm), tumor_type, biopsy_result, treatment, response_to_treatment, survival_status, combined_text, tumor_type_normalized`

**6. Integrity and Sanity Checks**

* Verified image and EHR file paths.
* Ensured no missing or invalid ICD codes.
* Confirmed 900 complete linked records with consistent survival and treatment fields.
* Checked duplicates (expected many-to-one links due to shared class images).

**7. Documentation**

* Prepared project documentation files under `/docs`, including dataset sources, cleaning steps, and challenges faced.

---

## Files Included

| File                   | Description                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| `01_data_prep.ipynb`   | Jupyter notebook for dataset preprocessing, cleaning, and linking. |
| `linked_brain_ehr.csv` | Final multimodal dataset combining EHR and MRI image data.         |
| `icd_lookup.csv`       | ICD-10 reference mapping table.                                    |
| `mapping.csv`          | Intermediate image–EHR mapping file.                               |
| `README.md`            | Main documentation summarizing project structure and deliverables. |

---

## Tools and Technologies

* Python 3
* Pandas, NumPy, Matplotlib, PIL
* Jupyter Notebook
* CSV Data Handling and Validation
* Image Processing and Integration with EHR Data

---

