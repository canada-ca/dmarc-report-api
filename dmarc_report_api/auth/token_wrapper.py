import jwt
import os

from graphql import GraphQLError


def decode_auth_token(request):
    """
    This function takes in a http requests and decodes the JWT sent by the user
    :param request: The http request sent from the user
    :return: Returns a list of dicts that contains the user claims
    """
    auth_header = request.headers.get("Authorization")
    try:
        payload = jwt.decode(
            auth_header,
            os.getenv("JWT_SECRET"),
            algorithms=["HS256"],
            options={"verify_exp": False},
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise GraphQLError("Signature expired, please request a new token.")
    except jwt.InvalidTokenError:
        raise GraphQLError("Invalid token, please request a new token.")


def require_token(method):
    def wrapper(self, *args, **kwargs):
        auth_resp = decode_auth_token(args[0].context)
        if isinstance(auth_resp, dict):
            api_token = auth_resp.get("api_token", None)
            if (api_token != os.getenv("TOKEN")) and (api_token is not None):
                raise GraphQLError("Error, Incorrect API Token")
            return method(self, *args, **kwargs)
        raise GraphQLError(auth_resp)

    return wrapper
