import asyncio
from agent import VoiceAgent
from app import app as fastapi_app

if __name__ == "__main__":
    agent = VoiceAgent()
    asyncio.run(agent.start())