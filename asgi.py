from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from llm import query_llm
from tts import synthesize_speech
import uvicorn
import os
import asyncio

app = FastAPI()

@app.get("/")
def index():
    return {"message": "S1m0ne (Simulation One) – Suppple AI Voice Assistant is active."}

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    text = data.get("query", "")
    user_id = data.get("user_id", "anonymous")
    response = await query_llm(text)
    return {"response": response}

@app.post("/tts")
async def tts(request: Request):
    data = await request.json()
    text = data.get("text", "")
    await synthesize_speech(text)
    return {"status": "tts_completed"}

@app.post("/log")
async def log_conversation(request: Request):
    data = await request.json()
    print(f"Conversation log: {data}")
    return JSONResponse(content={"status": "logged"})

if __name__ == "__main__":
    uvicorn.run("asgi:app", host="0.0.0.0", port=8000)
