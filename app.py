from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from livekit_token import generate_livekit_token

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/token")
def get_token(identity: str = Query("user", min_length=1)):
    try:
        token = generate_livekit_token(identity)
        return {
            "token": token,
            "url": "wss://s1m0n3-3g2pvo96.livekit.cloud"
        }
    except ValueError as e:
        return {"error": str(e)}