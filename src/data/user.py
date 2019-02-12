from src.data.base import MemRepo
from src.domain.model.user import User


class UserRepo(MemRepo):
    babel = (
        ("fname", "first_name"),
        ("lname", "last_name"),
        ("email_address", "email"),
        ("created", "created_at"),
    )

    domain_model = User
    table_name = "user"
