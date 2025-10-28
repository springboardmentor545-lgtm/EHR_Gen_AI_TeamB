# Data Cleaning Steps

## 1. Overview

This document summarizes the **data-cleaning, transformation, and preprocessing** operations performed on both **EHR** and **medical-imaging** datasets.
The objective was to standardize heterogeneous data sources, remove inconsistencies, and prepare a unified dataset suitable for multimodal AI model training.

---

## 2. EHR Data Cleaning

**Source:** Kaggle EHR Dataset (Gaurav Srivastav)
**File:** `ehr_dataset.csv`

### Steps Performed

1. **Data Import**

   ```python
   import pandas as pd
   df = pd.read_csv('ehr_dataset.csv')
   ```

   Loaded raw EHR data for inspection and structure validation.

2. **Null and Duplicate Removal**

   ```python
   df = df.dropna()
   df = df.drop_duplicates()
   ```

   Eliminated missing and duplicate records to ensure consistency.

3. **Text Normalization**

   ```python
   df.columns = df.columns.str.strip().str.lower()
   df['tumor_type'] = df['tumor_type'].str.lower().str.strip()
   ```

   * Standardized column names to lowercase.
   * Trimmed whitespace and corrected inconsistent capitalization.

4. **Data-Type Correction**
   Converted numeric fields to appropriate data types:

   ```python
   df['tumor_size(cm)'] = pd.to_numeric(df['tumor_size(cm)'], errors='coerce')
   ```

5. **Non-Informative Record Filtering**
   Removed records with invalid or placeholder text such as `"unknown"` in key fields, where necessary.

6. **Combined Text Field Creation**
   Merged relevant patient data into one text field for future NLP processing:

   ```python
   df['combined_text'] = (
       df['patient_id'].astype(str) + " " +
       df['age'].astype(str) + " " +
       df['gender'].astype(str) + " " +
       df['tumor_size(cm)'].astype(str) + " " +
       df['biopsy_result'] + " " +
       df['treatment'] + " " +
       df['response_to_treatment'] + " " +
       df['survival_status']
   )
   ```

7. **Export Cleaned Dataset**

   ```python
   df.to_csv('data/ehr_notes_processed/cleaned_ehr.csv', index=False)
   ```

   Saved the cleaned version for integration with imaging data.

---

## 3. Image Data Preprocessing

**Source:** Kaggle Brain Tumors Dataset (Mohammad Hossein)
**Classes:** glioma, meningioma, pituitary, notumor

### Steps Performed

1. **Folder Setup**

   ```
   data/raw/brain_tumors/
       ├── glioma/
       ├── meningioma/
       ├── pituitary/
       └── notumor/
   data/images_processed/
   ```

2. **Image Loading and Resizing**

   ```python
   from PIL import Image
   import os

   SRC = r'data/raw/brain_tumors'
   DST = r'data/images_processed'
   os.makedirs(DST, exist_ok=True)

   TARGET_SIZE = (256, 256)

   for cls in os.listdir(SRC):
       folder = os.path.join(SRC, cls)
       if os.path.isdir(folder):
           for fn in os.listdir(folder):
               if fn.lower().endswith(('.jpg', '.jpeg', '.png')):
                   img = Image.open(os.path.join(folder, fn)).convert('L')
                   img = img.resize(TARGET_SIZE)
                   outname = f"{cls.lower()}_{os.path.splitext(fn)[0]}.png"
                   img.save(os.path.join(DST, outname))
   ```

   * Converted to grayscale.
   * Resized uniformly to **256×256 px**.
   * Exported processed PNG images.

3. **File Verification**
   Confirmed that each processed image was accessible and viewable.
   Ensured uniform file naming and format.

---

## 4. ICD-10 Mapping Preparation

**File:** `icd_lookup.csv`

| Condition  | ICD-10 Code | Description                                           |
| ---------- | ----------- | ----------------------------------------------------- |
| glioma     | C71.9       | Malignant neoplasm of brain, unspecified              |
| meningioma | D32.9       | Benign neoplasm of meninges, unspecified              |
| pituitary  | D35.2       | Benign neoplasm of pituitary gland                    |
| notumor    | Z00.0       | General medical examination without abnormal findings |

### Processing Steps

1. Created a new CSV with columns `condition_keyword`, `icd10_code`, `icd10_description`.
2. Validated ICD codes using regex pattern `^[A-Z][0-9]{2}(\.[A-Z0-9]{1,4})?$`.
3. Linked ICD codes to each record based on diagnosis or tumor type.

---

## 5. Data Linking and Integration

Merged EHR, image, and ICD-10 data into a single structured file `linked_brain_ehr.csv`.

Key fields included:

```
file_id, image_path, ehr_path, diagnosis, icd10_code,
patient_id, age, gender, tumor_size(cm), tumor_type,
biopsy_result, treatment, response_to_treatment,
survival_status, combined_text, tumor_type_normalized
```

---

## 6. Integrity and Sanity Checks

Performed validation to ensure data consistency:

* Verified image and EHR paths exist.
* Checked ICD-10 code format and completeness.
* Confirmed no missing or null values.
* Duplicates identified (900 records) were expected due to many-to-one mapping.

---

## 7. Output Summary

| Output File            | Purpose                              |
| ---------------------- | ------------------------------------ |
| `cleaned_ehr.csv`      | Cleaned and standardized EHR records |
| `images_processed/`    | Preprocessed brain tumor images      |
| `icd_lookup.csv`       | ICD-10 mapping reference             |
| `linked_brain_ehr.csv` | Final multimodal linked dataset      |

---

## 8. Conclusion

The data cleaning and preprocessing workflow successfully standardized both EHR and imaging datasets.
All records were validated, ICD-10 codes applied correctly, and integrity checks passed.
The final dataset is fully prepared for use in **Milestone 2: Model Training and AI Integration**.

---

