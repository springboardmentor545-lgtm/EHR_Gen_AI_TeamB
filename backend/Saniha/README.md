# Milestone 1 – Individual Contribution (Saniha)

##  Overview
This folder contains my individual work for **Milestone 1** of our project **"Enhancing EHRs with GenAI"**.  
All code, datasets, and analysis in this section were developed and executed using **Google Colab**.

---
## Datasets Used

| Dataset | Description | Source |
|----------|--------------|--------|
| **Medical Transcriptions** | Contains real-world anonymized medical transcription reports. | [https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions](https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions) |
| **Chest X-Ray Images (Pneumonia)** | Chest X-ray images for pneumonia classification and analysis. | [https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) |

---

## Work Description
##  Tasks Completed
1. **EHR Text Cleaning:**
   - Processed over **4,999 medical transcription records**.
   - Removed null, duplicate, and non-informative entries.
   - Saved cleaned EHR text files in `/data/ehr_notes_processed`.

2. **ICD-10 Mapping:**
   - Created an `icd_lookup.csv` containing common diagnoses and their ICD-10 codes.
   - Matched EHR diagnoses to corresponding ICD-10 codes.
   - Saved final mappings in `mapping.csv`.

3. **Dataset Validation:**
   - Checked for missing or unmatched records.
   - Verified mappings for both images and EHR notes (no missing or invalid ICD codes).

4. **Output Files Generated:**
   - `mapping.csv` – final mapping between X-ray images, EHR notes, and ICD codes.
   - `icd_lookup.csv` – list of common ICD-10 references.
   - Cleaned EHR note files (`ehr_notes_processed` folder).

---

##  Files Included
| File | Description |
|------|--------------|
| `ehr_milestone1(saniha).ipynb` | Google Colab notebook containing dataset preparation, validation, and mapping code |
| `README.md` | Description of my contribution (this file) |


---

##  Tools & Technologies
- Python  
- Pandas, NumPy  
- Google Colab  
- CSV Data Handling  
- EHR + Image Data Integration  

---

##  Contributor
**Name:** Saniha Manjunath  
**Milestone:** 1 – Data Preprocessing and ICD Mapping  
**Project:** Enhancing EHRs with GenAI  (Team B)
**Repository Path:** `/backend/Saniha/`

---

Saniha/
  ├── ehr_milestone1(saniha).ipynb
  ├── dataset_sources.md
  ├── cleaning_steps.md
  ├── challenges.md
  └── README.md
