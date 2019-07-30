import json

from flask.views import View
from flask import Response, request

from src.rest.exceptions import AuthorizationError
from src.handler.auth import DecodeTokenHandler


class BaseView(View):
    def dispatch_request(self, **kwargs):
        try:
            self._authenticate()
            endpoint = getattr(self, request.method.lower())
            response = endpoint(request, **kwargs)
            response = self.to_json_response(response)
        except (TypeError, ValueError):
            response = self.respond(400, "Bad Request")
        except AuthorizationError:
            response = self.respond(403, "Unauthorized")
        except LookupError:
            response = self.respond(404, "Not Found")
        except Exception:
            response = self.respond(500, "Internal Server Error")

        return response

    def to_json_response(self, response):
        body = json.dumps(response.data)
        return self.respond(status=200, body=body, mimetype="application/json")

    def respond(self, status, body, mimetype="text/html"):
        return Response(status=status, response=body, mimetype=mimetype)

    def _authenticate(self):
        self._authenticate_token()

    def _authenticate_token(self):
        try:
            encoded_token = self._get_token_from_header()
            decode_token = DecodeTokenHandler()
            response = decode_token.run(encoded_token)
        except Exception as e:
            print(e)
            raise AuthorizationError("Invalid Token")

    def _get_token_from_header(self):
        authorization_header = request.headers.get("Authorization")
        if authorization_header is None:
            raise AuthorizationError("No token given")
        encoded_token = authorization_header.split(" ")[1]
        return encoded_token

    # TODO: bring key based authentication into the mix
    # def _authenticate_keys(self):
    #     try:
    #         public_key, private_key = self._get_keys_from_request()
    #         check_keys = CheckKeysHandler()
    #         response = check_keys.run(public_key, private_key)
    #     except Exception as e:
    #         return Response(success=False)
    #
    # def _get_keys_from_request(self):
    #     credentials = request.authentication
    #     public_key = credentials.username
    #     private_key = credentials.username
    #     return public_key, private_key
