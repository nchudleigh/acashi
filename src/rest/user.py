from src.rest.base import BaseView
from src.domain.case.user import GetUserUseCase


class UserView(BaseView):
    def get(self, request, key):
        response = GetUserUseCase().execute(key=key)
        return response

    def post(self):
        # return CreateUserUseCase.execute()
        raise NotImplementedError()

    def patch(self):
        # return UpdateUserUseCase.execute()
        raise NotImplementedError()

    def delete(self):
        # return DeleteUserUseCase.execute()
        raise NotImplementedError()
