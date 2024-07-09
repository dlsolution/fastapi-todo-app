from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.types import ASGIApp, Scope, Receive, Send
from locales import trans_pydantic_errors
from logger import logger
from app.exceptions.cmd_exception import CTFieldException, CTValidationException, CTException, \
    CTBadRequestException, CTUnauthorizedException, CTForbiddenException, CTNotFoundException, CTUnknownException
from utils.response import response_error

class ExceptionHandlerMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope['type'] != 'http':
            return await self.app(scope, receive, send)

        try:
            await self.app(scope, receive, send)
        except Exception as exception:
            logger.exception(exception)
            if isinstance(exception, RequestValidationError):
                errors = [
                    CTFieldException(
                        validation_type=error.get('type'),
                        validation_ctx=error.get('ctx', {}),
                        field='.'.join(error.get('loc', [])),
                    ) for error in trans_pydantic_errors(exception.errors())
                ]
                new_exception = CTValidationException(errors=errors)
            elif isinstance(exception, HTTPException):
                if exception.status_code == 400:
                    new_exception = CTBadRequestException(exception.detail)
                elif exception.status_code == 401:
                    new_exception = CTUnauthorizedException()
                elif exception.status_code == 403:
                    new_exception = CTForbiddenException()
                elif exception.status_code in [404, 405]:
                    new_exception = CTNotFoundException()
                else:
                    new_exception = CTUnknownException()
            elif isinstance(exception, CTException):
                new_exception = exception
            else:
                new_exception = CTUnknownException()

            await response_error(new_exception)(scope, receive, send)
