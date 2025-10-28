# 🧠 Enhancing EHRs with GenAI — Data Preprocessing Phase

## 📘 Overview
This project integrates **Electronic Health Records (EHRs)** and **medical imaging data** to create a unified, AI-ready dataset for disease prediction and clinical insight generation.  
The preprocessing phase focuses on data organization, cleaning, image transformation, and merging to ensure consistency and model-readiness.

---

## ⚙️ Process Summary
1. Mounted Google Drive and configured the project environment in Colab.  
2. Loaded `cancer_diagnosis_data.csv` and verified over 21k medical images.  
3. Preprocessed all images by:
   - Converting to grayscale  
   - Resizing to 256×256 pixels  
   - Saving optimized copies for model use  
4. Cleaned textual fields (diagnosis, description, notes) for uniformity.  
5. Automatically assigned **ICD-10 codes** based on diagnosis type:
   - Tumor → `C71.9`  
   - Normal → `Z00.0`  
   - Unknown → `UNKNOWN`  
6. Combined all cleaned data into a single structured file, `mapping.csv`.

---

## 📊 Results
- **Total Records:** 20,000  
- **Normal Images:** 3,066  
- **Tumor Images:** 18,651  
- **Missing Files:** 0  
- **Invalid ICD-10 Codes:** 0  

---

## 💡 Outcome
All preprocessing tasks have been successfully completed.  
The final dataset (`mapping.csv` + processed images) is now clean, validated, and ready for **model development and experimentation** in the next project phase.
