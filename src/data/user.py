from src.data import MemRepo
from src.domain.model.user import UserDTO


class UserRepo(MemRepo):
    DTO = UserDTO
    table_name = "user"
