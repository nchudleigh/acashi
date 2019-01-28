from src.domain.case.base import Case
from src.domain.model.user import User


class GetUserUseCase(Case):
    def run(self, key=None):
        if key is None:
            return

        user = self.repo.get_by_key(key)

        return User(
            key="user_x",
            first_name="Neil",
            last_name="Chudleigh",
            email="nchudleigh@gmail.com",
            created_at=1548617665812,
        )
