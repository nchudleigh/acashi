from src.domain.model import Model
from collections import namedtuple


PasswordDTO = namedtuple("Password", ["key", "hashed", "salt", "user_key"])


class Password(Model):
    DTO = PasswordDTO
