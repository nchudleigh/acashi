import json

from flask.views import View
from flask import Response, request

from src.rest.exceptions import AuthorizationError


class BaseView(View):
    def dispatch_request(self, **kwargs):
        try:
            endpoint = getattr(self, request.method.lower())
            response = endpoint(request, **kwargs)
            response = self.to_json_response(response)
        except (TypeError, ValueError):
            response = self.respond(400, "Bad Request")
            raise
        except AuthorizationError:
            response = self.respond(403, "Unauthorized")
            raise
        except LookupError:
            response = self.respond(404, "Not Found")
            raise
        except Exception:
            response = self.respond(500, "Internal Server Error")
            raise

        return response

    def to_json_response(self, response):
        body = json.dumps(response.data)
        return self.respond(status=200, body=body, mimetype="application/json")

    def respond(self, status, body, mimetype="text/html"):
        return Response(status=status, response=body, mimetype=mimetype)
