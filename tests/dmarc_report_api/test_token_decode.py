from flask import Request
from werkzeug.test import create_environ

from scripts.jwt_gen import jwt_gen

from dmarc_report_api.auth.token_wrapper import decode_auth_token


class TestTokenDecode:
    def test_token_decode(self):
        test_jwt = jwt_gen("some_random_string")

        environ = create_environ()
        environ.update(HTTP_AUTHORIZATION=test_jwt)
        request_headers = Request(environ)

        api_token = decode_auth_token(request_headers).get("api_token")

        assert api_token == "some_random_string"
