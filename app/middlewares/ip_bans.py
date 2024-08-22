from fastapi import (responses, Request, status)
from starlette.middleware.base import BaseHTTPMiddleware

class IPBanMiddleware(BaseHTTPMiddleware):
    def __init__(self, ip_bans:list, app):
        super().__init__(app)
        self.ip_bans = ip_bans

    async def dispatch(self, request: Request, call_next):
        print(request.client.host)
        if request.client.host in self.ip_bans:
            return responses.JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={"detail": "IP banned"},
            )
        return await call_next(request)