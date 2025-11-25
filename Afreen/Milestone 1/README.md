# Contribution for Module 1 (Backend)

## Overview
This folder contains my work for Module 1 of our project "Enhancing EHRs with GenAI".  
All code, datasets, and analysis in this section were developed and executed using Google Colab.

---

## Datasets Used
Dataset: EHR Dataset  
Description: 20,000 rows of cancer/tumor data  
Source: https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset  

Dataset: Brain Tumors MRI Dataset  
Description: ~21,672 JPEG images for brain tumor analysis  
Source: https://www.kaggle.com/datasets/mohammadhossein77/brain-tumors-dataset  

---

## Work Description
### Tasks Completed
1. EHR and Image Preprocessing:  
   - Processed 21,672 MRI images into 256x256 PNGs.  
   - Created 20,000 TXT notes from the EHR data.  

2. ICD-10 Mapping:  
   - Made an icd_lookup.csv with common diagnoses and ICD-10 codes.  
   - Mapped EHR diagnoses and image classes to ICD-10 codes in mapping.csv.  

3. Dataset Validation:  
   - Checked for missing or unmatched records.  
   - Verified mappings with no missing or invalid ICD-10 codes.  

4. Output Files Generated:  
   - mapping.csv – links 20,000 images and notes with codes.  
   - icd_lookup.csv – list of ICD-10 codes.  
   - Processed PNG images in data/images_processed/.  
   - TXT notes in data/ehr_notes_processed/.  

---

## Files Included
File: 01_data_prep.ipynb  
Description: Google Colab notebook with all my preprocessing, validation, and mapping code  
 

File: README.md  
Description: This file with my contribution details  

---

## Tools & Technologies
- Python  
- Pandas, NumPy, PIL  
- Google Colab  

---

## Contributor
Name: Afreen  
Milestone: 1 – Data Preprocessing and ICD Mapping  
Project: Enhancing EHRs with GenAI (Team B)  
Repository Path: /backend/Afreen/Milestone1/