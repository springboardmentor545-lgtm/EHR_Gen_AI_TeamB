# Enhancement Results – Milestone 2 (Vignesh M J)

## 1. Overview

This document provides a detailed report of the **medical image enhancement process** carried out in **Milestone 2** of the project *“Enhancing EHRs with GenAI.”*  
The enhancement phase aimed to improve the quality, contrast, and resolution of MRI brain images to assist with clearer visual analysis and AI-based diagnostic modeling.

---

## 2. Objective

To enhance preprocessed brain tumor MRI images using **AI-based super-resolution** techniques that improve detail visibility while preserving medical integrity.  
The enhanced images are intended to be used in subsequent stages for **diagnosis modeling** and **EHR–image fusion**.

---

## 3. Model Used

| Model | Type | Description |
|--------|------|--------------|
| **Real-ESRGAN (v0.3.0, Vulkan build)** | Super-Resolution GAN | Enhances low-resolution or blurred images to high resolution with improved clarity and reduced noise. Works fully offline using GPU acceleration. |

### Model Details

- **Executable:** `realesrgan-ncnn-vulkan.exe`  
- **Model File:** `realesrgan-x4plus.pth`  
- **Scale Factor:** ×4 (super-resolution)  
- **Input Format:** Grayscale MRI PNG images (256 × 256)  
- **Output Format:** Enhanced PNG images (1024 × 1024, downscaled for metrics)

---

## 4. Methodology

### Step 1 – Dataset Input
The preprocessed MRI brain tumor images from Milestone 1 were used for this task.
The dataset included four major tumor types: glioma, meningioma, pituitary, and notumor.
A total of 60 images were selected for enhancement — 15 images per class.
All input images were sourced from the directory:
data/images_processed/

### Step 2 – Enhancement Process
The Real-ESRGAN model was utilized to enhance image resolution and quality.
The enhancement process involved loading each image, applying super-resolution (4× scaling), and generating the enhanced output.
The process was executed locally using the realesrgan-ncnn-vulkan executable.
This approach ensured faster processing and better control over model execution.

### Step 3 – Output Storage
The enhanced images were automatically saved in the folder:
data/images_enhanced/
Each enhanced image retained the same filename as its corresponding input image for easy comparison.
The output folder was verified to contain all enhanced files with consistent naming and dimensions.

---

## 5. Evaluation

### Quantitative Analysis

Evaluated using **PSNR (Peak Signal-to-Noise Ratio)** and **SSIM (Structural Similarity Index)** on 10 sample pairs.

| Metric   | Average Value | Interpretation                                         |
| -------- | ------------- | ------------------------------------------------------ |
| **PSNR** | **32.48 dB**  | High-quality improvement; effective noise reduction    |
| **SSIM** | **0.918**     | Strong structural preservation and texture consistency |

### Qualitative Observations

| Parameter    | Observation                                                      |
| ------------ | ---------------------------------------------------------------- |
| **Clarity**  | Tumor boundaries are sharper and more distinguishable.           |
| **Noise**    | Significant reduction in background noise and blur.              |
| **Contrast** | Enhanced brightness and visibility of internal tissue patterns.  |
| **Details**  | Fine features preserved, supporting diagnostic interpretability. |


---

## 6. Tools and Libraries Used

| Tool / Library                 | Purpose                                |
| ------------------------------ | -------------------------------------- |
| **Real-ESRGAN (Vulkan build)** | Image enhancement and super-resolution |
| **Python 3.13**                | Programming and automation             |
| **Pillow (PIL)**               | Image preprocessing and conversion     |
| **scikit-image**               | PSNR & SSIM metric computation         |
| **Matplotlib**                 | Visualization and comparison           |
| **VS Code / Jupyter Notebook** | Development and testing environment    |

---

## 7. Key Findings

* Real-ESRGAN provided **significant visual improvement** without data distortion.
* Maintained **privacy and reproducibility** through offline processing.
* Quantitative results (PSNR > 32 dB, SSIM ≈ 0.92) indicate strong enhancement performance.
* Output images are now suitable for use in AI-based diagnostic and image classification models.

---

## 8. Comparison
* The the comparison result can be view in the "02_data_prep.ipynb" file


## 9. Conclusion

The **Real-ESRGAN enhancement pipeline** successfully improved MRI brain image clarity and detail.
The enhanced dataset demonstrates high-quality visual and structural consistency, supporting the next milestone’s objectives for **AI-assisted diagnosis and EHR-image analysis.**

---

