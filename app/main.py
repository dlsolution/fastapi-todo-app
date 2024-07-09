from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.exceptions import RequestValidationError
from app.api.middlewares.exception_handlers import ExceptionHandlerMiddleware
from config.config import Settings, get_settings
from typing_extensions import Annotated
from app import api
from .api.middlewares.authentication import AuthenticationMiddleware

def init_exception_handlers(app_: FastAPI) -> None:
    def raise_all_exceptions(request: Request, exception: Exception):
        raise exception
    # # Overrides Fastapi default exception handlers to raise all exceptions to our exception handler middleware
    app_.add_exception_handler(HTTPException, raise_all_exceptions)
    app_.add_exception_handler(RequestValidationError, raise_all_exceptions)
    # Our exception handler is handled in a middleware
    app_.add_middleware(ExceptionHandlerMiddleware)


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


def init_middlewares(app_: FastAPI) -> None:
    app_.add_middleware(AuthenticationMiddleware)


def init_routers(app_: FastAPI) -> None:
    app_.include_router(api.router)


def create_app() -> FastAPI:
    app_ = FastAPI()
    init_exception_handlers(app_)
    init_middlewares(app_)
    init_routers(app_)
    return app_


app = create_app()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=400, detail="This is a bad request")
    return {"item_id": item_id}


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
