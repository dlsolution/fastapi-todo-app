from fastapi import Request
from jose import JWTError, jwt
from starlette.types import ASGIApp, Scope, Receive, Send
from config.config import get_settings
from utils.utils import get_token
from starlette.authentication import AuthCredentials


settings = get_settings()

class AuthenticationMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        auth_scopes = []
        user = {'is_authenticated': False}
        
        if scope['type'] == 'http':
            token = get_token(Request(scope))
            if token:
                try:
                    payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.algorithm])
                    email = payload.get("sub", "")
                    role = payload.get("role", "")
                    user_profile = {"email": email, "role": role}
                    auth_scopes.extend(['authenticated', 'user'])
                    user = {
                        'is_authenticated': True,
                        'profile': user_profile,
                    }
                except JWTError:
                    None
        
        scope['auth'] = AuthCredentials(auth_scopes)
        scope['user'] = user
        
        await self.app(scope, receive, send)
