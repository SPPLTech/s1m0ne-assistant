# Created by Suppple AI Team
import os
import httpx

async def synthesize_speech(text):
    url = os.getenv("CARTESIA_TTS_URL")
    headers = {
        "Authorization": f"Bearer {os.getenv('CARTESIA_TTS_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {"text": text, "voice": "default"}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        audio_url = response.json().get("audio_url")
        if audio_url:
            print(f"Audio response at: {audio_url}")
        else:
            print("Failed to generate speech.")
