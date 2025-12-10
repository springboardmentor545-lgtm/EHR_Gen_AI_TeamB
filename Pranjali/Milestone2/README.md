📘 Milestone 2 – Medical Image Enhancement
AI-Powered Enhanced EHR Imaging & Documentation System

This milestone focuses on improving the quality of medical images using classical computer vision techniques and evaluating their enhancement performance. The enhanced images will later support diagnostic ML models and structured reporting.

🚀 Objectives

Load the cleaned dataset from Milestone 1

Apply medical-grade enhancement techniques

Visualize Before vs After results

Compute quality metrics (PSNR, SSIM)

Save enhanced images and evaluation outputs

📂 Dataset Used
This milestone uses the mapping.csv file generated in Milestone 1, which contains:
| Column     | Description                          |
| ---------- | ------------------------------------ |
| image_path | File path to each preprocessed image |
| diagnosis  | Medical condition label              |
| modality   | Type of scan (X-ray/MRI/CT)          |
| patient_id | Traceability metadata                |

🛠️ Methods Used
1. CLAHE (Contrast Limited Adaptive Histogram Equalization)

Enhances local contrast

Widely used in X-ray, CT, and MRI preprocessing

2. Non-Local Means Denoising

Removes noise while preserving edges

Useful for MRI & CT scans

3. Evaluation Metrics

PSNR (Peak Signal-to-Noise Ratio)

SSIM (Structural Similarity Index)

Quantifies clarity and structural improvements

📊 Workflow Summary
🔹 Step 1: Load Mapping File

Load mapping.csv and prepare the enhancement output directory.

🔹 Step 2: Apply Enhancement Functions

Applied image enhancement using:

CLAHE

Denoising

Optional sharpening

🔹 Step 3: Save Enhanced Images

10 sample images processed and saved for documentation.

🔹 Step 4: Visualize Before vs After

Side-by-side visualization for qualitative evaluation.

🔹 Step 5: Compute Metrics

Generated PSNR & SSIM for each enhanced image and computed averages.

🔹 Step 6: Save Results

All evaluation metrics saved as:enhancement_metrics.csv
