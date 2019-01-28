from src.rest.base import BaseView
from src.domain.case.get_user import GetUserUseCase
from src.data.mem_repo import UserMemRepo


class UserView(BaseView):
    def get(self, request, key):
        repo = UserMemRepo()
        case = GetUserUseCase(repo).run(key=key)
        return "ok"

    def post(self):
        # return CreateUserUseCase.run()
        raise NotImplementedError()

    def patch(self):
        # return UpdateUserUseCase.run()
        raise NotImplementedError()

    def delete(self):
        # return DeleteUserUseCase.run()
        raise NotImplementedError()
