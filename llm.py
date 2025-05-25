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
