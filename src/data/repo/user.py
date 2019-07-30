from src.data.repo.base import BaseRepo
from src.data.dao.user import UserDAO
from src.domain.entity.user import UserEntity


class UserRepo(BaseRepo):
    def get(self, key):
        user_dao = UserDAO.get(key)
        return self.to_entity(user_dao)
