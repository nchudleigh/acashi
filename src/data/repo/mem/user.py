from src.data.repo.mem.base import MemRepo
from src.domain.model.user import User


class UserMemRepo(MemRepo):
    babel = (
        ("fname", "first_name"),
        ("lname", "last_name"),
        ("email_address", "email"),
        ("created", "created_at"),
    )

    domain_model = User

    def get_by_key(self, key):
        user = self._get("User", "key", key)
        return self.to_domain(user)
