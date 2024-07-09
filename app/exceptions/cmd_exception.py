from typing import List
import i18n

from constants import ERROR_ID_UNKNOWN, ERROR_ID_BAD_REQUEST, ERROR_ID_NOT_FOUND, ERROR_ID_UNAUTHENTICATED, \
    ERROR_ID_FORBIDDEN, ERROR_ID_RESOURCE_NOT_FOUND, ERROR_ID_SERVER_ERROR, ERROR_ID_VALIDATION_REQUIRED, \
    ERROR_ID_VALIDATION_WRONG_FORMAT, ERROR_ID_VALIDATION_WRONG_TYPE, ERROR_ID_VALIDATION_IN_ENUM


class CTException(Exception):
    def __init__(self, error_id: str = ERROR_ID_UNKNOWN, **kwargs):
        self.error = {
            'error_id': error_id,
            'title': i18n.t('errors.{error_id}.title'.format(error_id=error_id)),
            'message': i18n.t('errors.{error_id}.message'.format(error_id=error_id)) + f' ({error_id})',
        }
        self.need_report = False
        for key in kwargs:
            self.error[key] = kwargs[key]

        if error_id == ERROR_ID_BAD_REQUEST:
            self.status_code = 400
        elif error_id == ERROR_ID_UNAUTHENTICATED:
            self.status_code = 401
        elif error_id == ERROR_ID_FORBIDDEN:
            self.status_code = 403
        elif error_id == ERROR_ID_NOT_FOUND or error_id == ERROR_ID_RESOURCE_NOT_FOUND:
            self.status_code = 404
        else:
            self.status_code = 500

    def to_dict(self):
        dict_data = self.error

        child_errors = self.error.get('errors')
        if child_errors:
            child_error_data = []
            for child_error in child_errors:
                if isinstance(child_error, CTException):
                    child_error_data.append(child_error.to_dict())
            dict_data['errors'] = child_error_data

        return dict_data


class CTFieldException(CTException):
    def __init__(self, validation_type: str, validation_ctx: dict, field: str, title: str = None, message: str = None):
        error_parses = validation_type.split('.')
        error_base_name = error_parses[0] if error_parses else None
        error_code = None
        if error_parses and len(error_parses) == 2:
            error_code = error_parses[1]
        elif error_parses and len(error_parses) == 3:
            error_code = error_parses[2]

        if error_base_name == 'value_error':
            if error_code == 'missing' or (error_code == 'min_length' and validation_ctx.get('limit_value') == 1):
                error_id = ERROR_ID_VALIDATION_REQUIRED
            elif error_code in ['regex', 'max_digits', 'decimal_places', 'min_length', 'max_length']:
                error_id = ERROR_ID_VALIDATION_WRONG_FORMAT
            else:
                error_id = ERROR_ID_VALIDATION_WRONG_TYPE
        elif error_base_name == 'type_error':
            if error_code == 'enum':
                error_id = ERROR_ID_VALIDATION_IN_ENUM
            else:
                error_id = ERROR_ID_VALIDATION_WRONG_TYPE
        else:
            error_id = ERROR_ID_VALIDATION_WRONG_FORMAT

        super().__init__(error_id, field=field)

        if title:
            self.error['title'] = title
        if message:
            self.error['message'] = f'{message} ({error_id})'


class CTValidationException(CTException):
    def __init__(self, errors: List[CTFieldException]):
        super().__init__(ERROR_ID_BAD_REQUEST, errors=errors)


class CTBadRequestException(CTException):
    def __init__(self, detail: str):
        super().__init__(ERROR_ID_BAD_REQUEST, detail=detail)


class CTUnauthorizedException(CTException):
    def __init__(self):
        super().__init__(ERROR_ID_UNAUTHENTICATED)


class CTForbiddenException(CTException):
    def __init__(self):
        super().__init__(ERROR_ID_FORBIDDEN)


class CTNotFoundException(CTException):
    def __init__(self):
        super().__init__(ERROR_ID_NOT_FOUND)


class CTServerException(CTException):
    def __init__(self):
        super().__init__(ERROR_ID_SERVER_ERROR)
        self.need_report = True


class CTUnknownException(CTException):
    def __init__(self):
        super().__init__(ERROR_ID_UNKNOWN)
        self.need_report = True


class CTResourceNotFoundException(CTException):
    def __init__(self):
        super().__init__(ERROR_ID_RESOURCE_NOT_FOUND)
