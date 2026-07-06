"""
setup_check.py
--------------
Run this BEFORE `streamlit run app.py` to confirm:
1. Python version is OK
2. All required packages import successfully
3. .env file exists with a GROQ_API_KEY set

Usage:
    python setup_check.py
"""

import sys
import os
import importlib

print("=" * 60)
print("AI Interview Coach — Setup Check")
print("=" * 60)

# 1. Python version
print(f"\n[1/3] Python version: {sys.version.split()[0]}")
if sys.version_info < (3, 9):
    print("    WARNING: Python 3.9+ recommended.")
else:
    print("    OK")

# 2. Package imports
print("\n[2/3] Checking required packages...")
packages = {
    "streamlit": "streamlit",
    "groq": "groq",
    "pdfplumber": "pdfplumber",
    "dotenv": "python-dotenv",
    "streamlit_mic_recorder": "streamlit-mic-recorder",
}

missing = []
for module_name, pip_name in packages.items():
    try:
        importlib.import_module(module_name)
        print(f"    OK   - {pip_name}")
    except ImportError:
        print(f"    MISSING - {pip_name}")
        missing.append(pip_name)

if missing:
    print(f"\n  Run this to install missing packages:")
    print(f"  pip install {' '.join(missing)}")
else:
    print("\n  All packages installed correctly.")

# 3. .env / API key check
print("\n[3/3] Checking .env file...")
if not os.path.exists(".env"):
    print("    MISSING - .env file not found in this folder.")
    print("    Run: cp .env.example .env   (then edit it with your key)")
else:
    from dotenv import load_dotenv
    load_dotenv()
    key = os.getenv("GROQ_API_KEY")
    if not key or "your_groq_api_key_here" in key:
        print("    .env file found, but GROQ_API_KEY is not set properly.")
        print("    Open .env and paste your real key from console.groq.com")
    else:
        print(f"    OK   - GROQ_API_KEY is set ({key[:8]}...hidden)")

print("\n" + "=" * 60)
if not missing and os.path.exists(".env"):
    print("Setup looks good. Run: streamlit run app.py")
else:
    print("Fix the items marked above, then re-run this script.")
print("=" * 60)
