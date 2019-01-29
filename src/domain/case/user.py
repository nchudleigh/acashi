from src.domain.case.base import Case, Response
from src.domain.model.user import User
from src.data.repo.mem.user import UserMemRepo


class GetUserUseCase(Case):
    def run(self, key=None):
        if key is None:
            return

        user = UserMemRepo().get_by_key(key)

        return Response(user.to_dict())
