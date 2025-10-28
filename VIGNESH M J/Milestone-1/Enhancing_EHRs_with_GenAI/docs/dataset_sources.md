# Dataset Sources

## 1. EHR Dataset

**Name:** EHR Dataset
**Source:** [Kaggle – EHR Dataset (Gaurav Srivastav)](https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset)
**Description:**
This dataset contains anonymized electronic health records (EHR) representing patient-level tumor data.
Each record includes details such as patient ID, age, gender, tumor size, biopsy results, treatment type, response to treatment, and survival status.
The dataset serves as the **textual (EHR) component** of the project, supporting ICD-10 mapping and structured data integration.

**License:** Publicly available for educational and research purposes.
**Data Collected:** 20,000 records (subset cleaned and processed for use).
**Date Accessed:** October 2025
**Usage in Project:**

* Cleaned using Pandas to remove duplicates and missing values.
* Normalized and linked with brain tumor image classes.
* Final cleaned version stored in `data/ehr_notes_processed/cleaned_ehr.csv`.

---

## 2. Imaging Dataset

**Name:** Brain Tumors Dataset
**Source:** [Kaggle – Brain Tumors Dataset (Mohammad Hossein)](https://www.kaggle.com/datasets/mohammadhossein77/brain-tumors-dataset)
**Description:**
This dataset provides MRI brain images categorized into four classes:

* Glioma
* Meningioma
* Pituitary
* Notumor

A subset of **15 images per class (60 total)** was selected to create a manageable dataset for preprocessing and integration with EHR data.
All images were resized to **256 × 256 pixels**, converted to grayscale, and saved in `data/images_processed/`.

**License:** Public dataset under Kaggle terms of use; de-identified and open for educational research.
**Data Collected:** 60 images (subset extracted from original dataset).
**Date Accessed:** October 2025
**Usage in Project:**

* Served as the **visual (imaging) component** for model development.
* Linked with EHR records based on tumor type classification.
* Used in generating the multimodal dataset (`linked_brain_ehr.csv`).

---

## 3. ICD-10 Reference Data

**Name:** ICD-10 Mapping Table (Custom Created)
**Source:** [World Health Organization – ICD-10 Classification](https://icd.who.int/browse10/2019/en)
**Description:**
A reference table (`icd_lookup.csv`) was manually constructed to map disease names to their corresponding ICD-10 codes.
The ICD-10 codes provide standardized diagnostic identifiers to support model training and automated code prediction.

| Condition  | ICD-10 Code | Description                                           |
| ---------- | ----------- | ----------------------------------------------------- |
| Glioma     | C71.9       | Malignant neoplasm of brain, unspecified              |
| Meningioma | D32.9       | Benign neoplasm of meninges, unspecified              |
| Pituitary  | D35.2       | Benign neoplasm of pituitary gland                    |
| Notumor    | Z00.0       | General medical examination without abnormal findings |

**License:** Public domain (WHO classification data).
**Usage in Project:**

* Used to assign ICD-10 codes to each EHR record based on tumor type.
* Validated via regex format check to ensure proper code syntax.
* Linked as part of the multimodal dataset for downstream AI tasks.

---

## 4. Data Integration Summary

| Component        | Source               | Processed Output       | Purpose                                 |
| ---------------- | -------------------- | ---------------------- | --------------------------------------- |
| EHR Text Data    | Kaggle EHR Dataset   | `cleaned_ehr.csv`      | Structured patient-level health records |
| Medical Images   | Brain Tumor Dataset  | `images_processed/`    | Processed MRI brain tumor images        |
| ICD-10 Codes     | WHO ICD-10 Reference | `icd_lookup.csv`       | Diagnostic coding reference             |
| Combined Dataset | Derived Integration  | `linked_brain_ehr.csv` | Final linked EHR–Image dataset          |

---

## 5. Data Ethics and Compliance

* All datasets used are **publicly available and de-identified**.
* No personally identifiable information (PII) was used or retained.
* The project complies with data ethics guidelines for educational research.
* Datasets are used solely for **non-commercial, academic, and model-development** purposes.

---