from functools import wraps

from flask import jsonify, make_response
from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims


def admin_required(fn, roles):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if not list(set(claims) & set(roles)):
            return make_response(jsonify(error='You do not have sufficient permission to access this resource!'), 403)
        else:
            return fn(*args, **kwargs)

    return wrapper
