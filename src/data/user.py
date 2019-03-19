from src.data.base import MemRepo
from src.domain.model.user import UserDTO


class UserRepo(MemRepo):
    babel = (
        ("fname", "first_name"),
        ("lname", "last_name"),
        ("email_address", "email"),
        ("created", "created_at"),
    )

    DTO = UserDTO
    table_name = "user"
