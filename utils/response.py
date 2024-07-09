import math
from starlette.responses import JSONResponse
from app.exceptions.cmd_exception import CTException


def response_item(item) -> dict:
    return {
        'data': item,
    }


def response_pagination(items: list, limit: int, total=0, page=1) -> dict:
    return {
        'data': {
            'items': items,
            'pagination': {
                'limit': limit,
                'total': total,
                'page': int(page),
                'total_page': math.ceil(int(total)/int(limit))
            },
        },
    }


def response_error(exception: CTException):
    return JSONResponse({
        'error': exception.to_dict()
    }, status_code=exception.status_code)
