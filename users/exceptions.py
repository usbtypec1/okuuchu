from rest_framework import status
from rest_framework.exceptions import APIException

__all__ = ('UserAlreadyExistsError',)


class UserAlreadyExistsError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_code = 'user_already_exists'
    default_detail = 'User with this email already exists.'
