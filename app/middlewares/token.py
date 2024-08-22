from fastapi import (responses, Request, status)
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

class TokenAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, activate:bool, app):
        super().__init__(app)
        self.activate = activate

    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        print(request.headers)
        print(request.client.host)
        print(request.client)
        print(request.url)
        print(request.method)
        if (not token) and self.activate:
            return responses.JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Missing token"},
            )
        return await call_next(request)