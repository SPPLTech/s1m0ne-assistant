# Created by Suppple AI Team
import os
import httpx

async def query_llm(text):
    url = os.getenv("CEREBRAS_API_URL")
    headers = {
        "Authorization": f"Bearer {os.getenv('CEREBRAS_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {"prompt": text, "max_tokens": 100}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        data = response.json()
        return data.get("completion", "I'm here to help.")

import os
import requests


def query_llm(prompt):
    # Order of fallbacks: Cerebras > GPT-4 > DeepSeek > Qwen
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
