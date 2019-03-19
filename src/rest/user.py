from src.rest.base import BaseView
from src.handler.user import GetUserHandler, CreateUserHandler


"""
This layer is a very very thin translation from the http handlers to the arguments
that our Action expects.
It does not handle _anything_ application specific.  It is simply an adapter to our handlers.
It can handle the response object (our domain output DTO) and translate it back to JSON.
"""


class UserView(BaseView):

    # NOTE: these are going to be really repetitive
    # a higher level class would make sense to abstract this
    def get(self, request):
        handler = GetUserHandler()
        response = handler.go(request.data)
        return response

    def post(self, request):
        handler = CreateUserHandler()
        response = handler.go(request.data)
        return response

    def patch(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()
