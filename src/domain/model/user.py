from src.domain.model.base import Model


class User(Model):
    def __init__(self, key, first_name, last_name, email):
        self.key = key
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at

    def from_dict(self, dict_):
        self.key = dict_.get("key")
        self.first_name = dict_.get("first_name")
        self.last_name = dict_.get("last_name")
        self.email = dict_.get("email")
        self.created_at = dict_.get("created_at")
