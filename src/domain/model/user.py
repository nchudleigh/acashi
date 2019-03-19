from src.domain.model.base import Model
from collections import namedtuple


UserDTO = namedtuple(
    "UserDTO", ["key", "first_name", "last_name", "email", "created_at"]
)


class User(Model):
    DTO = UserDTO

    def __init__(self, **kw):
        self._fields = self.DTO._fields
        for field in self._fields:
            setattr(self, field, kw[field])

    def to_dto(self):
        return self.DTO([getattr(self, field) for field in self._fields])
