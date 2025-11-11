# Milestone 2 – Individual Contribution (Vignesh M J)

## Overview

This document outlines my individual contribution for **Milestone 2** of the project *“Enhancing EHRs with GenAI.”*  
The primary focus of this phase was on **medical image enhancement and quality evaluation** to improve the diagnostic clarity of brain MRI images linked with Electronic Health Records (EHRs).  
All tasks were implemented locally using **Python (Jupyter Notebook and VS Code)** with the **Real-ESRGAN** enhancement framework.

---

## Datasets Used

| Dataset | Description | Source |
|----------|--------------|---------|
| **Brain Tumor MRI Images** | Dataset containing MRI scans across four classes — *glioma*, *meningioma*, *pituitary*, and *no tumor*. Used for enhancement and quality assessment. | [Kaggle – Brain Tumors Dataset (Mohammad Hossein)](https://www.kaggle.com/datasets/mohammadhossein77/brain-tumors-dataset) |
| **EHR Dataset** | Synthetic dataset containing anonymized patient tumor data, treatment history, and survival details. Linked to imaging data from Milestone 1. | [Kaggle – EHR Dataset (Gaurav Srivastav)](https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset) |

---

## Work Description

### **1. Image Enhancement Model Selection**

* Selected **Real-ESRGAN (v0.3.0, Vulkan build)** for super-resolution and denoising.  
* Chosen for its high restoration quality and offline functionality.  
* Supports efficient GPU acceleration on standard hardware (Intel Iris Xe).

---

### **2. Local Setup and Execution**

* Downloaded and configured the Real-ESRGAN executable (`realesrgan-ncnn-vulkan.exe`).  
* Enhanced 60 preprocessed MRI images (15 per tumor type).  
* Executed enhancement locally.
* Process completed offline, averaging ~2 seconds per image.
* Enhanced images stored in `data/images_enhanced/`.

---

### **3. Visual Validation**

* Displayed side-by-side comparisons of original vs. enhanced images using **Matplotlib**.
* Verified noticeable improvements in:

  * Image clarity and contrast
  * Sharper tumor boundaries
  * Reduced blur and noise
* Demonstrated five random image pairs for qualitative review.

---

### **4. Quantitative Evaluation**

* Computed **PSNR (Peak Signal-to-Noise Ratio)** and **SSIM (Structural Similarity Index)** using `scikit-image`.
* Compared 10 representative images from different tumor categories.

| Metric   | Average Value | Interpretation                                                                    |
| -------- | ------------- | --------------------------------------------------------------------------------- |
| **PSNR** | **32.48 dB**  | Strong improvement in overall clarity and noise reduction                         |
| **SSIM** | **0.918**     | Excellent structural similarity preservation between original and enhanced images |

* Metrics confirm that Real-ESRGAN effectively enhances diagnostic quality while maintaining tissue integrity.

---

### **5. Documentation**

* Recorded methodology, parameters, and evaluation results in `docs/enhancement_results.md`.
* Added output samples and before-after visualizations for reference.
* Updated project structure to include the `images_enhanced` directory.

---

## Files Included

| File / Folder                | Description                                                    |
| ---------------------------- | -------------------------------------------------------------- |
| `02_image_enhancement.ipynb` | Jupyter Notebook for image enhancement and metric computation. |
| `data/images_enhanced/`      | Folder containing ESRGAN-enhanced MRI images.                  |
| `enhancement_results.md`     | Detailed methodology, results, and visual comparisons.         |
| `README.md`                  | Summary of Milestone 2 contributions and outcomes.             |

---

## Tools and Technologies

* **Python 3.13**
* **Pillow (PIL)** – image preprocessing and resizing
* **scikit-image** – PSNR & SSIM evaluation
* **Matplotlib** – visualization and comparison
* **Real-ESRGAN (Vulkan build)** – offline image enhancement
* **VS Code / Jupyter Notebook** – development and testing environments

---

## Challenges Faced

* Compatibility issues while installing the PyTorch-based ESRGAN model — resolved by switching to the lightweight **Vulkan executable version**.
* Initial mismatch in output filenames and image dimensions — corrected through automatic resizing before metric computation.
* ESRGAN online model was not available.

---

## Summary

In **Milestone 2**, the Real-ESRGAN pipeline successfully enhanced all MRI brain tumor images used in *Enhancing EHRs with GenAI.*
The process achieved:

* **High fidelity output** with improved clarity (PSNR > 32 dB).
* **Strong structural consistency** (SSIM ≈ 0.92).
* **Completely offline execution**, ensuring data privacy and reproducibility.

The enhanced dataset will now support **Milestone 3**, which focuses on AI-driven diagnosis and intelligent linkage between imaging and EHR data.

---

