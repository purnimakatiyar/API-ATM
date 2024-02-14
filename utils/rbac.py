import functools
from flask_smorest import abort
from flask_jwt_extended import get_jwt
from flask_jwt_extended import verify_jwt_in_request
 
def role_access(roles: list):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            verify_jwt_in_request()
            payload = get_jwt()
            if payload["role"] in roles:
                return func(*args, **kwargs)
            else:
                abort (403, message="Unauthorised request")
        return inner
    return wrapper