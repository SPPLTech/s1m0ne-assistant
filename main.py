import asyncio
from agent import VoiceAgent

if __name__ == "__main__":
    agent = VoiceAgent()
    asyncio.run(agent.start())
