import os
import google.generativeai as genai
from pathlib import Path

env_path = Path(".env").resolve()
api_key = None
if env_path.exists():
    with open(env_path, "r", encoding="utf-8-sig") as f:
        for line in f:
            if "GEMINI_API_KEY=" in line:
                api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                break

genai.configure(api_key=api_key)
print("Models available for your API key:\n")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")
