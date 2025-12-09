# backend/app/notes.py

import os
import json
import time
import re
import pandas as pd
from glob import glob
from datetime import datetime
from pathlib import Path

# -----------------------------
# ICD-10 Lookup Configuration
# -----------------------------
ICD_LOOKUP_PATH = "data/icd_lookup.csv"
lookup_df = pd.read_csv(ICD_LOOKUP_PATH)


def find_icd10(text: str):
    """
    Basic keyword matching using icd_lookup.csv
    """
    matches = []
    for _, row in lookup_df.iterrows():
        if row['condition_keyword'].lower() in text.lower():
            matches.append({
                "code": row['icd10_code'],
                "description": row['icd10_description']
            })
    return matches or [{"code": "R69", "description": "Illness, unspecified"}]


# ==========================================================
# LLM (Gemini) — REAL IMPLEMENTATION
# ==========================================================

import google.generativeai as genai

API_KEY = "apikey_goes_here"
MODEL_NAME = "gemini-2.5-flash"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)


def llm_generate_note(prompt: str) -> str:
    """
    Calls Gemini API and returns the generated text output.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Gemini API Error: {str(e)}")


# ==========================================================
# Main Note Generation Logic (Uses LLM + ICD Mapping)
# ==========================================================

def build_prompt(patient: dict):
    """
    Structured prompt for Gemini. Ensures clean JSON output.
    """
    prompt = f"""
You are a medical documentation assistant. Generate a structured JSON object ONLY.

Required keys:
- patient_id
- note : concise 3–6 sentence clinical summary
- icd10_code : single most relevant ICD-10 code
- icd10_description
- recommended_steps : list of next steps (max 5)
- reasoning : 1-2 sentences of justification

Patient data:
{json.dumps(patient, indent=2)}
"""
    return prompt.strip()


def clean_json_output(raw: str):
    """
    Extract valid JSON from messy LLM output.
    """
    match = re.search(r"(\{[\s\S]*\})", raw)
    if match:
        candidate = match.group(1)
        candidate = re.sub(r",\s*}", "}", candidate)
        candidate = re.sub(r",\s*\]", "]", candidate)
        try:
            return json.loads(candidate)
        except:
            return None
    try:
        return json.loads(raw)
    except:
        return None


def generate_note(input_json: dict):
    """
    Generates a structured medical note using Gemini LLM
    AND performs ICD-10 code validation via lookup table.
    """

    prompt = build_prompt(input_json)
    raw_output = llm_generate_note(prompt)

    parsed = clean_json_output(raw_output)

    if parsed is None:
        # Fallback: minimal safe structure
        parsed = {
            "patient_id": input_json["patient_id"],
            "note": raw_output[:400],
            "icd10_code": "R69",
            "icd10_description": "Illness, unspecified",
            "recommended_steps": ["Review full LLM output.", "Re-run generation."],
            "reasoning": "Failed to parse Gemini JSON output.",
            "raw_output": raw_output
        }

    # ICD override using lookup
    icd_from_lookup = find_icd10(parsed.get("note", ""))
    if icd_from_lookup:
        parsed["icd10_code"] = icd_from_lookup[0]["code"]
        parsed["icd10_description"] = icd_from_lookup[0]["description"]

    return parsed
