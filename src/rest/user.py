from src.rest.base import BaseView
from src.handler.user import GetUserHandler, CreateUserHandler


"""
This layer is a very very thin translation from the http handlers to the arguments
that our Action expects.
It does not handle _anything_ application specific.  It is simply an adapter to our handlers.
It can handle the response object (our domain output DTO) and translate it back to JSON.
"""

# NOTE: these CRUD endpoints are going to be really repetitive
# a higher level class would make sense for this pattern
class CreateUserView(BaseView):
    name = "user_create"
    path = "/users"

    def post(self, request):
        handler = CreateUserHandler()
        response = handler.run(key)
        return response


class UserView(BaseView):
    name = "users"
    path = "/users/<key>"

    def get(self, request, key):
        handler = GetUserHandler()
        response = handler.run(key)
        return response

    def patch(self, request, key):
        raise NotImplementedError()

    def delete(self, request, key):
        raise NotImplementedError()
