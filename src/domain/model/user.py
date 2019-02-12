from src.domain.model.base import Model


class User(Model):
    def __init__(
        self, key=None, first_name=None, last_name=None, email=None, created_at=None
    ):
        self.key = key
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at

    def to_dict(self):
        return vars(self)
