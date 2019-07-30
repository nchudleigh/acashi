from src.domain.entity.base import BaseEntity


class UserEntity(BaseEntity):
    __attributes__ = ["key", "created_at", "name"]
