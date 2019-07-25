from src.domain.model import Model
from collections import namedtuple


UserDTO = namedtuple(
    "UserDTO", ["key", "first_name", "last_name", "email", "created_at"]
)


class User(Model, UserDTO):
    def validate(self):
        pass
