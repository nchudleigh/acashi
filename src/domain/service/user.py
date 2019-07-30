from src.domain.service.base import BaseService
from src.domain.entity.user import UserEntity


class UserService(BaseService):
    def create(self):
        return UserEntity(key=key, created_at=created_at, name=name)
