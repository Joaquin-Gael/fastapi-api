from fastapi import (responses, Request, status)
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware
from rich.pretty import pprint
from datetime import datetime

class TokenAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, activate:bool, app):
        super().__init__(app)
        self.activate = activate

    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        pprint(request)
        pprint("Headers:")
        pprint(dict(request.headers))
        pprint(f"IP: {request.client.host}")
        pprint(f"Port: {request.client.port}")
        pprint(f"Url: {request.url}")
        pprint(f"Url Query: {request.url.query}")
        pprint(f"Method: {request.method}")
        pprint(f"Date: {datetime.now()}")
        pprint(f"Token: {token}")
        if (not token) and self.activate:
            return responses.JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Missing token"},
            )
        return await call_next(request)