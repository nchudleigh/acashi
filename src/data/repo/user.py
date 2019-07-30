from src.data.repo.base import BaseRepo
from src.data.dao.user import UserDAO
from src.domain.entity.user import UserEntity


class UserRepo(BaseRepo):
    dao = UserDAO
    entity = UserEntity

    def create(self, entity):
        dao = self.to_dao(entity)
        # add to session?
        return dao
