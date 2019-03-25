from src.domain.model import Model
from collections import namedtuple


AuthDTO = namedtuple("AuthDTO", ["user_key"])


class Auth(Model):
    DTO = AuthDTO
