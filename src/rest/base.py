from flask.views import View
from flask import Response
from flask import request


class BaseView(View):
    def dispatch_request(self, **kwargs):
        return getattr(self, request.method.lower())(request, **kwargs)

    def register(self, app, name, path):
        self.app = app
        self.path = path
        self.name = name
        self.view_func = self.as_view(name)

        # if the class method is found, register it as a route
        for method in ["GET", "POST", "DELETE", "PATCH"]:
            if callable(getattr(self, method.lower())):
                self.register_route(methods=[method])

    def register_route(self, methods):
        self.app.add_url_rule(self.path, view_func=self.view_func, methods=methods)

    def BadRequestResponse(self, message="Your request ain't right"):
        return self.response(400, message)

    def UnauthorizedResponse(self, message="You can't go here"):
        return self.response(401, message)

    def NotFoundResponse(self, message="Couldn't find that, you sure that it exists?"):
        return self.response(404, message)

    def response(self, status, message, data=None):
        return Response(status=status, response=message)
