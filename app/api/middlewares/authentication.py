from fastapi import Request
from jose import JWTError, jwt
from starlette.types import ASGIApp, Scope, Receive, Send
from app.exceptions.cmd_exception import CTUnauthorizedException
from utils.response import response_error
from logger import logger
from config.config import get_settings

settings = get_settings()


EXCLUDE_PATHS = [
    ("/docs", "GET"),
    ("/favicon.ico", "GET"),
    ("/openapi.json", "GET"),
    ("/info", "GET"),
    ("/v1/login", "POST"),
    ("/v1/users", "POST")
]

class AuthenticationMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope['type'] != 'http':
            return await self.app(scope, receive, send)
        
        request = Request(scope, receive)
        request_path = request.url.path
        request_method = request.method
        if any(path == request_path and method == request_method for path, method in EXCLUDE_PATHS):
            return await self.app(scope, receive, send)
        
        authorization = request.headers.get("Authorization", "")
        if not authorization or not authorization.startswith("Bearer "):
            new_exception = CTUnauthorizedException()
            logger.exception(new_exception)
            return await response_error(new_exception)(scope, receive, send)
        
        token = authorization.split("Bearer ")[1]
        try:
            payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.algorithm])
            scope['user'] = payload
        except JWTError:
            new_exception = CTUnauthorizedException()
            logger.exception(new_exception)
            return await response_error(new_exception)(scope, receive, send)
        
        await self.app(scope, receive, send)
