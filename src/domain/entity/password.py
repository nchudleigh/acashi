from src.domain.entity.base import BaseEntity


class PasswordEntity(BaseEntity):
    __attributes__ = ["key", "user_key", "created_at", "salt", "hashed_password"]
