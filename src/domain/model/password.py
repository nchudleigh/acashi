from src.domain.model import Model
from collections import namedtuple


PasswordDTO = namedtuple("Password", ["key", "hashed", "salt", "user_key"])


class Password(Model):
    DTO = PasswordDTO

    def get_by_user_key(self, user_key):
        self.get("user_key", user_key)
