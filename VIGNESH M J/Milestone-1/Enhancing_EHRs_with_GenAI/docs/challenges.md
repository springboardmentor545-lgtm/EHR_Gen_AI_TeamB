# Challenges Faced

## 1. Large Dataset Handling

The original brain-tumor imaging dataset was over 250 MB in size, which made full-scale downloading and preprocessing impractical on a local system.
To address this, I selected a **smaller, representative subset of 15 images per class** (glioma, meningioma, pituitary, notumor) to maintain diversity while ensuring manageable storage and faster execution.

---

## 2. Manual Data Acquisition

The original brain-tumor imaging dataset was over 250 MB in size.
All required datasets were therefore downloaded manually, verified, and placed into the structured folder hierarchy.
This ensured data integrity but required additional organization time.

---

## 3. Linking EHR and Image Data

The EHR dataset and the brain-tumor image dataset originated from **different sources** and lacked shared patient identifiers.
I established a logical mapping strategy using the **tumor type** field as a bridge between the two datasets.
This produced a **many-to-one mapping**, where multiple EHRs corresponded to a single tumor-class image, which had to be validated carefully during integrity checks.

---

## 4. ICD-10 Reference Errors

During early preprocessing, the ICD lookup table produced parsing errors because of inconsistent commas and extra columns.
I resolved this by rebuilding the `icd_lookup.csv` with clearly defined headers:
`condition_keyword, icd10_code, icd10_description`.
This correction allowed successful ICD-10 matching for all tumor classes.

---

## 5. Duplicate Record Interpretation

The integrity script initially flagged **900 duplicate entries**.
After review, these were confirmed to be **expected duplicates** caused by repeated class-based mappings rather than actual data redundancy.
This finding was documented to avoid confusion during evaluation.

---

## 6. Environment and Path Issues

Some initial image-path mismatches occurred because of backward-slash and case-sensitivity inconsistencies.
I standardized all paths and extensions to lowercase and used absolute Windows paths to eliminate these issues.

---


## Summary

Despite encountering multiple data-handling and compatibility challenges, I successfully completed all preprocessing, linking, and validation tasks for Milestone 1.
The final linked dataset integrates **EHR, imaging, and ICD-10 code data** accurately, providing a clean, reliable foundation for AI model development in subsequent milestones.

---
