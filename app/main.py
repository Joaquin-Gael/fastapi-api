from fastapi import (FastAPI, responses, Request)
from .middlewares.token import TokenAuthMiddleware, CORSMiddleware
from .middlewares.ip_bans import IPBanMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TokenAuthMiddleware,
    activate = False
    )

app.add_middleware(
    IPBanMiddleware,
    ip_bans=[],
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}