import os
import requests

def query_llm(prompt):
    endpoints = [
        ("Cerebras", os.getenv("CEREBRAS_API_URL")),
        ("OpenAI", os.getenv("OPENAI_API_URL")),
        ("DeepSeek", os.getenv("DEEPSEEK_API_URL")),
        ("Qwen", os.getenv("QWEN_API_URL"))
    ]
    for name, url in endpoints:
        if url:
            try:
                print(f"⚙️  Querying {name}...")
                response = requests.post(url, json={"prompt": prompt})
                response.raise_for_status()
                return response.json().get("response", "[No response from LLM]")
            except Exception as e:
                print(f"⚠️  {name} failed: {e}")
                continue
    return "Apologies, all AI services are currently unavailable."
