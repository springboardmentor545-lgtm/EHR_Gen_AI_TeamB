# Contribution for Module 2 (Image Enhancement – Real-ESRGAN)

## Overview
This folder contains my work for Module 2 of our project "Enhancing EHRs with GenAI".
All code execution, model loading, and image enhancement were done using Google Colab.

---

## Datasets Used
Dataset: Brain Tumors MRI Dataset
Description: ~21,672 MRI images used for enhancement
Source: https://www.kaggle.com/datasets/mohammadhossein77/brain-tumors-dataset

Dataset: EHR Dataset
Description: 20,000 rows of EHR notes (used only for validation and mapping continuity)
Source: https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset

---

## Work Description
### Tasks Completed
1. Mapping Validation and Path Fixing
   - Loaded mapping.csv and validated required columns.
   - Replaced incorrect prefix paths and ensured the images point to the processed directory.
   - Checked for missing files in the dataset.

2. Image Resolution Verification
   - Confirmed that processed MRI images are 256x256.
   - Reported any incorrect-resolution images.

3. Real-ESRGAN Setup in Colab
   - Installed realesrgan==0.3.0 and necessary libraries.
   - Downloaded pretrained weights (RealESRGAN_x4plus.pth).
   - Implemented the RRDB and RRDBNet architecture in PyTorch.
   - Loaded the official pretrained ESRGAN model and moved it to GPU mode.

4. Sampling and Enhancement of MRI Images
   - Selected 15 sample MRI images from dataset.
   - Saved originals in /data/original/.
   - Enhanced all 15 images using Real-ESRGAN.
   - Saved enhanced outputs in /data/enhanced/.

5. Visualization (Before vs After)
   - Created a comparison grid of all 15 images.
   - Saved the figure as before_vs_after_grid.png in the results folder.

6. Image Quality Evaluation (PSNR & SSIM)
   - Computed PSNR and SSIM for each pair (original vs enhanced).
   - Stored detailed metrics in psnr_ssim_detailed.txt.

7. Exporting Final Files
   - Copied the ESRGAN model file into /models/.
   - Stored all results (grid image, metrics, enhanced images) under /results/.

---

## Files Included
File: 02_enhancing_images.ipynb
Description: Main Colab notebook with model setup, enhancement pipeline, visualization, and metric computation.

Enhanced MRI samples: enhanced_images
Original MRI samples: original_images

---

## Tools & Technologies
Python
PyTorch
Real-ESRGAN
OpenCV, PIL, NumPy
Google Colab

---

## Contributor
Name: Afreen
Milestone: 2 – Real-ESRGAN Image Enhancement
Project: Enhancing EHRs with GenAI (Team B)
Repository Path: /backend/Afreen/milestone2/