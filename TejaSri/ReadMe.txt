Contribution for Module 1 (frontend)

Overview
This folder contains the work for Module 1 of the project "Enhancing EHRs with GenAI". The code, dataset handling, and analysis were developed and executed using Google Colab, as detailed in the Jupyter notebook `EHR_AI_Milestone_1.ipynb`.

Datasets Used

Dataset: EHR Dataset  
Description: 20,000 rows of cancer/tumor data  
Source: https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset  

Dataset: Brain Tumors MRI Dataset  
Description: ~21,672 JPEG images for brain tumor analysis  
Source: https://www.kaggle.com/datasets/mohammadhossein77/brain-tumors-dataset  

Work Description
Tasks Completed
1. EHR and Image Preprocessing:  
   Processed 21,672 MRI images into 256x256 PNGs, stored in `data/images_processed/`.  
   Generated 20,000 TXT notes from EHR data, saved in `data/ehr_notes_processed/`.  

2. ICD-10 Mapping:  
   Created `icd_lookup.csv` containing common diagnoses and their corresponding ICD-10 codes.  
   Mapped EHR diagnoses and image classes to ICD-10 codes in `mapping.csv`.  

3. Dataset Validation:  
   Performed integrity checks for missing images, notes, or unmatched records, identifying 16,934 missing/unknown diagnoses but no invalid ICD-10 codes.  
   Conducted sanity checks to ensure no duplicate `file_id` entries or orphaned notes.  

4. Output Files Generated:  
   `mapping.csv`: Links 20,000 images and notes with ICD-10 codes.  
   `icd_lookup.csv`: Contains ICD-10 code mappings.  
   Processed PNG images in `data/images_processed/`.  
   TXT notes in `data/ehr_notes_processed/`.  

Files Included
File: EHR_AI_Milestone_1.ipynb  
Description: Google Colab notebook containing code for dataset downloading, folder structure setup, image and EHR preprocessing, ICD-10 mapping, and data validation.  

File: README.md  
Description: This file summarizing the contribution details for Module 1.  

Tools & Technologies
Python  
Pandas, NumPy, PIL  
Google Colab  

Contributor
Name: Tejasri Nakka  
Milestone: 1 – Data Preprocessing and ICD Mapping  
Project: Enhancing EHRs with GenAI (Team B)  
Repository Path: /TejaSri/
