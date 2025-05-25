import datetime
import os
import jwt

def generate_livekit_token(identity: str = "user", ttl_seconds: int = 3600):
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")
    if not api_key or not api_secret:
        raise ValueError("LIVEKIT_API_KEY and LIVEKIT_API_SECRET must be set in environment variables")

    now = datetime.datetime.utcnow()
    exp = now + datetime.timedelta(seconds=ttl_seconds)

    payload = {
        "iss": api_key,
        "sub": identity,
        "nbf": int(now.timestamp()),
        "exp": int(exp.timestamp()),
        "video": {
            "roomCreate": True,
            "roomJoin": True,
            "canPublish": True,
            "canSubscribe": True
        }
    }

    token = jwt.encode(payload, api_secret, algorithm="HS256")
    return token