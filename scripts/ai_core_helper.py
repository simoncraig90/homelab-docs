#!/usr/bin/env python3
"""
ai_core_helper.py
A simple wrapper for sending prompts to the AI-Core VM (Ollama) and returning clean results.
"""

import json
import urllib.request

# Update this if the AI-Core IP changes
AI_CORE_URL = "http://192.168.0.147:11434/api/generate"
MODEL_NAME = "qwen2.5:14b-instruct"

def ask_ai_core(prompt: str) -> str:
    """
    Send a prompt to AI-Core and return the clean text response (no JSON / streaming chunks).
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,    # Return a single JSON response instead of multiple chunks
    }

    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        AI_CORE_URL,
        data=data,
        headers={"Content-Type": "application/json"},
    )

    with urllib.request.urlopen(request) as response:
        raw = response.read().decode("utf-8")

    result = json.loads(raw)
    return result.get("response", "").strip()


# --------------------- OPTIONAL: Quick CLI mode --------------------- #
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: ./ai_core_helper.py 'your question or text here'")
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    answer = ask_ai_core(question)
    print(answer)
