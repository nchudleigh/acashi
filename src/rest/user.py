from src.rest.base import BaseView
from src.action.user import GetUserAction


"""
This layer is a very very thin translation from the http handlers to the arguments
that our Action expects.
It does not handle _anything_ application specific.  It is simply an adapter to our actions.
It can handle the response object (our domain output DTO) and translate it back to HTTP land.
"""


class UserView(BaseView):
    def get(self, request, key):
        return GetUserAction(key)

    def post(self):
        # return CreateUserUseCase.execute()
        raise NotImplementedError()

    def patch(self):
        # return UpdateUserUseCase.execute()
        raise NotImplementedError()

    def delete(self):
        # return DeleteUserUseCase.execute()
        raise NotImplementedError()
