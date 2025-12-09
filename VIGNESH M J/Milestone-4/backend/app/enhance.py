# backend/app/enhance.py
import tempfile
import subprocess
import os
import shutil
from pathlib import Path
from PIL import Image
import io

# Path to your Real-ESRGAN executable
REALESRGAN_EXE = r"C:/Users/vigne/OneDrive/Desktop/EHR/milestone4/models/realesrgan-ncnn-vulkan.exe"
RETAION_DEFAULT_MODEL = "realesrgan-x4plus"
DEFAULT_TIMEOUT_SECS = 60  # tune as needed

def enhance_image_local(img_bytes: bytes, model: str = RETAION_DEFAULT_MODEL, timeout: int = DEFAULT_TIMEOUT_SECS) -> bytes:
    """
    - Writes the incoming bytes to a temporary input path
    - Calls realesrgan-ncnn-vulkan (or other binary) to produce output
    - Reads the output bytes and returns them
    - Uses a timeout, raises exception on error
    """
    tmp_dir = tempfile.mkdtemp(prefix="enhance_")
    try:
        in_path = Path(tmp_dir) / "input.png"
        out_path = Path(tmp_dir) / "output.png"

        # Save input image bytes
        with open(in_path, "wb") as f:
            f.write(img_bytes)

        # If the exe is not present, raise a helpful error
        if not Path(REALESRGAN_EXE).exists():
            # optional fallback: if user wants to run a python-based SR instead, hook here
            raise FileNotFoundError(f"Enhancer executable not found at {REALESRGAN_EXE}")

        # Build subprocess command
        # Note: the exe may accept folder inputs — adjust based on your binary.
        cmd = [
            str(REALESRGAN_EXE),
            "-i", str(in_path),
            "-o", str(out_path),
            "-n", model,
            "-s", "4"
        ]

        # Run and enforce timeout
        completed = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)

        if completed.returncode != 0:
            stderr_text = completed.stderr.decode(errors="ignore")
            raise RuntimeError(f"Enhancer failed (rc={completed.returncode}): {stderr_text}")

        # Read output bytes
        if not out_path.exists():
            raise RuntimeError("Enhancer did not produce output file")

        with open(out_path, "rb") as f:
            enhanced_bytes = f.read()

        # Optionally, ensure output is a valid image (PIL can open)
        try:
            Image.open(io.BytesIO(enhanced_bytes)).verify()
        except Exception:
            raise RuntimeError("Enhanced output is not a valid image")

        return enhanced_bytes

    finally:
        # best-effort cleanup
        try:
            shutil.rmtree(tmp_dir)
        except Exception:
            pass
