import json

from flask.views import View
from flask import Response, request


class BaseView(View):
    def register(self, app, name, path):
        self.app = app
        self.path = path
        self.name = name
        self.view_func = self.as_view(name)

        # if the class method is found, register it as a route
        for method in ["get", "post", "delete", "patch", "put"]:
            if hasattr(self, method) and callable(getattr(self, method)):
                self.register_route(methods=[method.upper()])

    def register_route(self, methods):
        self.app.add_url_rule(self.path, view_func=self.view_func, methods=methods)

    def dispatch_request(self, **kwargs):
        try:
            method = getattr(self, request.method.lower())
            response = endpoint(request, **kwargs)
        except (TypeError, ValueError):
            return self.respond(400, "Bad Request")
        except AuthorizationError:
            return self.respond(403, "Unauthorized")
        except NotFoundError:
            return self.respond(404, "Not Found")
        except Exception:
            return self.respond(500, "Internal Server Error")

        return self.to_json_response(response)

    def to_json_response(self, response):
        body = json.dumps(response.data)
        return self.respond(status=200, body=body, mimetype="application/json")

    def respond(self, status, body, mimetype="text/html"):
        return Response(status=status, response=body, mimetype=mimetype)
