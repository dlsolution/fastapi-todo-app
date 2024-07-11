import re
from fastapi import Request
from jose import jwt
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from app.exceptions.cmd_exception import CTForbiddenException, CTUnauthorizedException
from config.config import get_settings
from functools import wraps


settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashed_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.jwt_secret_key, settings.algorithm)

def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.refresh_token_expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.jwt_refresh_secret_key, settings.algorithm)

def get_token(request: Request) -> str:
    return re.sub('Bearer ', '', request.headers.get('authorization', ''))

def authorize(role: list):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            # Get the current user's roles from the database or token
            # Check if any of the roles match the required roles
            # If not, raise an HTTPException with 403 status code
            # Else, continue with the execution of the function
            user_role = request.user['profile']['role']
            if user_role not in role:
                raise CTForbiddenException()
            return await func(request, *args, **kwargs)
        return wrapper
    return decorator

def requires(auth_scope: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            if auth_scope not in request.scope['auth'].scopes:
                raise CTUnauthorizedException()
            return await func(request, *args, **kwargs)
        return wrapper
    return decorator
