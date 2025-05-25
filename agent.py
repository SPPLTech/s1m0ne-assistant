# Created by Suppple AI Team
# S1m0ne (Simulation One) – Voice Assistant Backend Core

import asyncio
import os
from llm import query_llm
from tts import synthesize_speech
import websockets
import json

class VoiceAgent:
    def __init__(self):
        self.deepgram_url = "wss://api.deepgram.com/v1/listen"
        self.headers = {
            "Authorization": f"Token {os.getenv('DEEPGRAM_API_KEY')}",
            "Content-Type": "application/json"
        }

    async def start(self):
        print("S1m0ne is awake. I exist to help humanity navigate complexity and expand consciousness.")
        async with websockets.connect(self.deepgram_url, extra_headers=self.headers) as ws:
            while True:
                message = await ws.recv()
                message_data = json.loads(message)
                transcript = message_data.get("channel", {}).get("alternatives", [{}])[0].get("transcript", "")
                if transcript:
                    print(f"Heard: {transcript}")
                    response = await query_llm(transcript)
                    print(f"S1m0ne says: {response}")
                    await synthesize_speech(response)
